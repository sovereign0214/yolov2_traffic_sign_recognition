# yolov2_traffic_sign_recognition
開發無人車的路標辨識API，並將其搭載在硬體上，實現實時物件偵測。 首先蒐集龐大的路標影像資料集，分類、對其做標籤，接著使用Darkflow + tiny-yolo-voc深度學習捲積類神經網路模型進行修改、訓練，訓練後的結果能夠準確找出路標位置以及辨識路標。我們已將完成的軟體實作在PC、樹莓派與TX2中，透過相機，將資料即時傳入主機進行處理，能夠實現實時物件偵測。此外，除了實時的版本，在電腦上播放影片或照片等，也可透過畫面擷取來進行偵測。
