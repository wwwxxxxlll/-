from elasticsearch_dsl import DocType, Date, Completion, Keyword, Text, Integer

from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer

from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=["localhost"])

class CustomAnalyzer(_CustomAnalyzer):
    def get_analysis_definition(self):
        return {}

ik_analyzer = CustomAnalyzer("ik_max_word", filter=["lowercase"])
class TextItem(DocType):   
    suggest = Completion(analyzer=ik_analyzer)#es的completion类型，用于智能联想
    title = Text(analyzer="ik_max_word")#Text(analyzer……)用于分词实现全文搜索
    create_date = Date()
    url = Keyword()
    abstract = Text(analyzer="ik_max_word")
    keywords = Text(analyzer="ik_max_word")
    journal  = Keyword()
    language = Keyword()
    author = Keyword()
    class Meta:
        index = "data"
        doc_type = "article"


if __name__ == "__main__":
    TextItem.init()