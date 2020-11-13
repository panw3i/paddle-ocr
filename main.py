import paddlehub as hub 
ocr = hub.Module(name="chinese_ocr_db_crnn_mobile") #加载预训练模型
results = ocr.recognize_text(paths=['/Users/pan/PycharmProjects/paddle-ocr/test.png'], visualization=True)  #输入自定义待识别图片路径、并保存可视化图片结果

print(results)