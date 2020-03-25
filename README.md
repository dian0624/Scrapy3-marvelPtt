#Scrapy3-marvelPtt
技術點:
1. Scrapy框架

    找出URL規律作為翻頁**URL的拼接**，輸入欲爬取頁數訪問頁面獲取響應，構建Selector選擇器**xpath匹配**並判斷抓取標題、po文用戶名、po文時間、推文數，
    將**資料儲存為csv檔**。
  
    新增UserAgent文件且在middleware中使用random模塊隨機使用UserAgent，打開settings中的MIDDLEWARES通道。
    
------------------------------------------------------------------    
功能說明: 

使用Scrapy框架爬取Ptt-marvel版，並且設置多個User-Agent隨機使用，
爬取標題、po文用戶名、po文時間、推文數，並且將資料儲存為csv檔。

![image](https://github.com/dian0624/Scrapy3-marvelPtt/blob/master/1585111491343.jpg)




