# MedSSL-Semi-Supervised-Learning-for-Medical-Data
Utilizing semi-supervised learning, specifically FixMatch, on medical data like X-ray images from ChestX-ray dataset. Enhancing model accuracy with ChexNet architecture for improved lung pathology classification.
## Authors

Mateusz Krakowski

Bartosz Latosek

## Client note
Semi-supervised learning and medical data
The problem of semi-supervised learning occurs when we have data at our disposal, only some of which has been correctly described by experts. This problem often occurs in medical data where case reports are very expensive. Then it is worth using additional, undescribed data that can help learn more general features.
The task involves the implementation of one of the best performing SSL methods - FixMatch: https://github.com/google-research/fixmatch in the problem of semi-supervised classification of medical data - X-ray images of the lungs appearing in the ChestX-ray set https://openaccess.thecvf. com/content_cvpr_2017/papers/Wang_ChestX-ray8_Hospital-Scale_Chest_CVPR_2017_paper.pdf
https://nihcc.app.box.com/v/ChestXray-NIHCC
To improve the quality of the model, it is worth using an architecture dedicated to this type of data, e.g. chexnet https://github.com/arnoweng/CheXNet?tab=readme-ov-file
As part of the task, you must independently prepare the ChestX-ray set for the semi-supervised learning problem and adapt the FixMatch method accordingly.

## Client note original (PL)
Wpół nadzorowane uczenie a dane medyczne. Problem wpółnadzorowanego uczenia występuje gdy mamy do dyspozycji dane z których tylko część została poprawnie opisana przez ekspertów. Problem ten często występuje w danych medycznych gdzie opis przypadków jest bardzo kosztowny. Wówczas warto wykorzystać dodatkowe, nieopisane dane które mogą pomóc nauczyć się bardziej generalnych cech. 
Zadanie polega na implementacji jednej z najlepiej działających metod SSLowych - FixMatch: https://github.com/google-research/fixmatch w problemie klasyfikacji wpółnadzorowanej danych medycznych - zdjęć rentenowskich płuc występujących w zbiorze ChestX-ray https://openaccess.thecvf.com/content_cvpr_2017/papers/Wang_ChestX-ray8_Hospital-Scale_Chest_CVPR_2017_paper.pdf 
https://nihcc.app.box.com/v/ChestXray-NIHCC 
Dla poprawy jakości modelu warto wykorzystać architekturę dedykowaną do tego typu danych np. chexnet https://github.com/arnoweng/CheXNet?tab=readme-ov-file 
W ramach zadania należy samodzielnie przygotować zbiór ChestX-ray do problemu wpółnadzorowanego uczenia i odpowiednio dostosować metodę FixMatch
