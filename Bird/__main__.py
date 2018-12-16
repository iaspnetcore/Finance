from Export import ExpModule
from Stock import TrendAnalyzer
from DataBase import TdxData


def addBeginEndToTimeList(Begin, End, TimeList):
    if Begin != TimeList[0]:
        TimeList.insert(0, Begin)
    if End != TimeList[-1]:
        TimeList.append(End)

def main():
    startTime = '2018/09/01-00:00'
    endTime = '2018/12/14-00:00'
    DataPath = r'.\StockData'
    ID_ZS_SH = '399300'
    NAME_ZS_SH = '沪深300'
    ID_BK = 'Categorys'

    # 获取数据
    Tdx = TdxData.TdxDataEngine(DataPath)
    filePath = Tdx.GetTdxFileList()
    File_SH = Tdx.SearchInFileList(filePath,'',ID_ZS_SH)
    File_BK = Tdx.SearchInFileList(filePath,ID_BK, '')
    Data_SH = Tdx.HandlerTdxDataToList(File_SH,startTime,endTime)
    Data_BK = Tdx.HandlerTdxDataToList(File_BK,startTime,endTime)

    # 分析数据
    T = TrendAnalyzer.Trend()
    tData = T.StockDataList2DataFrame(Data_SH[0][NAME_ZS_SH])
    tData_RE = T.Candlestick_RemoveEmbodySeqMode(tData)

    # # k线
    # T.Candlestick_Drawing(tData_RE)

    # 分析分型， 返回分型 顶底时间列表, 返回结果为2维数组
    typeTimeList = T.Candlestick_TypeAnalysis(tData_RE,True)

    TimeList = []
    for item in typeTimeList:
        TimeList.append(item[0])

    listRange = T.calcPriceRange(Data_BK, TimeList)     # 按时间轴，计算数据波段涨幅
    ExpModule.FormatData2TXT(TimeList,listRange)        # 波段涨幅，降序，输出到Data.txt 导入 excel 模板，分析使用

if __name__ == '__main__':
    main()