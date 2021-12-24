import json
import redis
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from elasticsearch import Elasticsearch

from search.models import TextItem

client = Elasticsearch(hosts=["127.0.0.1"])#连本地
redis_cli = redis.StrictRedis()#建一个k-v映射池

class IndexView(View):
    def get(self,request):
        print(redis_cli)
        redis_cli.set("fuck","u")
        d = redis_cli.get('fuck')
        print(d)
        topn = redis_cli.zrevrangebyscore("search_keywords_set","+inf","-inf",start=0,num=5)#提高推荐分，没有就建一个关键词，赋分为0
        top_n = (word.decode() for word in topn)#转utf-8编码
        return render(request, "index.html",{"top_n":top_n})
class SearchView(View):
    def get(self, request):
        key_words = request.GET.get("key", "")#关键词

        #redis_cli.zincrby("search_keywords_set", key_words)#增加推荐度

        topn = redis_cli.zrevrangebyscore("search_keywords_set","+inf","-inf",start=0,num=5)
        top_n = (word.decode() for word in topn)
        page = request.GET.get("p", "")#页数（关键词也要传，且不变）
        try:
            page = int(page)
        except:
            page = 1

        #jobbole_count = redis_cli.get("jobbole_count")
        start_time = datetime.now()
        response = client.search(
            index="data",
            body={
                "query": {
                    "multi_match": {
                        "query": key_words,
                        "fields": ["标题", "作者", "关键词","期刊名称","摘要"]
                    }
                },
                "from": (page - 1) * 10,
                "size": 10,
                "highlight": {
                    "pre_tags": ['<span class="keyWord">'],
                    "post_tags": ['</span>'],
                    "fields": {
                        "标题":{}, "作者":{}, "关键词":{},"期刊名称":{},"摘要":{}
                    }
                }
            }
        )
        end_time = datetime.now()
        last_seconds = (end_time - start_time).total_seconds()
        total_nums = response["hits"]["total"]
        if (page % 10) > 0:
            page_nums = int(total_nums / 10) + 1
        else:
            page_nums = int(total_nums / 10)
        hit_list = []
       
        for hit in response["hits"]["hits"]:
                hit_dict = {}
                if "标题" in hit['highlight']:
                    hit_dict["标题"] = "".join(hit['highlight']["标题"])
                else:
                    hit_dict["标题"] = hit["_source"]["标题"]
                if "keywords" in hit["highlight"]:
                    hit_dict["关键词"] = "".join(hit["highlight"]["关键词"])[:500]
                else:
                    hit_dict["关键词"] = hit["_source"]["关键词"][:500]
                hit_dict["url"] = hit["_source"]["url"]
                hit_dict["score"] = hit["_score"]

                hit_list.append(hit_dict)
        

        return render(request, "index.html", {"page": page,
                                               "all_hits": hit_list,
                                               "key_words": key_words,
                                               "total_nums": total_nums,
                                               "page_nums": page_nums,
                                               "last_seconds": last_seconds,
                                               "top_n":top_n})
class SearchSuggest(View):
    def get(self, request):
        key_words = request.GET.get('s', '')
        re_datas = []
        if key_words:
            s = TextItem.search()
            s = s.suggest('my_suggest', key_words, completion={
                "field": "suggest", "fuzzy": {
                    "fuzziness": 2#前两个字不变
                },
                "size": 10
            })
            suggestions = s.execute_suggest()#不行就换成s.execute()试试
            for match in suggestions.my_suggest[0].options:
                source = match._source
                re_datas.append(source["title"])
            result = json.dumps(re_datas)#返回建议
            return render(request,'index.html',{'result':result})