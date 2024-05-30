# MedSSL-Semi-Supervised-Learning-for-Medical-Data

Utilizing semi-supervised learning, specifically FixMatch, on medical data like X-ray images from ChestX-ray dataset. Enhancing model accuracy with ChexNet architecture for improved lung pathology classification.

## Authors

Mateusz Krakowski

Bartosz Latosek

## Client note

Semi-supervised learning and medical data
The problem of semi-supervised learning occurs when we have data at our disposal, only some of which has been correctly described by experts. This problem often occurs in medical data where case reports are very expensive. Then it is worth using additional, undescribed data that can help learn more general features.
The task involves the implementation of one of the best performing SSL methods - FixMatch: https://github.com/google-research/fixmatch in the problem of semi-supervised classification of medical data - X-ray images of the lungs appearing in the ChestX-ray set https://openaccess.thecvf.com/content_cvpr_2017/papers/Wang_ChestX-ray8_Hospital-Scale_Chest_CVPR_2017_paper.pdf
https://nihcc.app.box.com/v/ChestXray-NIHCC
To improve the quality of the model, it is worth using an architecture dedicated to this type of data, e.g. chexnet https://github.com/arnoweng/CheXNet?tab=readme-ov-file
As part of the task, you must independently prepare the ChestX-ray set for the semi-supervised learning problem and adapt the FixMatch method accordingly.

## Client note original (PL)

Wpół nadzorowane uczenie a dane medyczne. Problem wpółnadzorowanego uczenia występuje gdy mamy do dyspozycji dane z których tylko część została poprawnie opisana przez ekspertów. Problem ten często występuje w danych medycznych gdzie opis przypadków jest bardzo kosztowny. Wówczas warto wykorzystać dodatkowe, nieopisane dane które mogą pomóc nauczyć się bardziej generalnych cech.
Zadanie polega na implementacji jednej z najlepiej działających metod SSLowych - FixMatch: https://github.com/google-research/fixmatch w problemie klasyfikacji wpółnadzorowanej danych medycznych - zdjęć rentenowskich płuc występujących w zbiorze ChestX-ray https://openaccess.thecvf.com/content_cvpr_2017/papers/Wang_ChestX-ray8_Hospital-Scale_Chest_CVPR_2017_paper.pdf
https://nihcc.app.box.com/v/ChestXray-NIHCC
Dla poprawy jakości modelu warto wykorzystać architekturę dedykowaną do tego typu danych np. chexnet https://github.com/arnoweng/CheXNet?tab=readme-ov-file
W ramach zadania należy samodzielnie przygotować zbiór ChestX-ray do problemu wpółnadzorowanego uczenia i odpowiednio dostosować metodę FixMatch


## Project Organization

---

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

---

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>


Dziękuję za dokumentację wstępną. Mam wrażenie że zupełnie nie zrozumieli Panowie o co chodzi w problemie semi-supervised learning, nie przeczytali Panowie jak działa metoda FixMatch którą mają Panowie dostosować i nie sprawdzili Panowie jak wygląda zbiór ChestX-ray. 
- Zbiór ChestX-ray jest w pełni opisany, Panów zadanie polega na dostosowanie go do problemu SSL - zasymulowanie (w rozsądny spsób) braku niektórych anotacji (analogicznie do tego co znajduje się w artykule opisującym FixMatcha)
- "Przed przystąpieniem do trenowania docelowego modelu, należy znaleźć sposób na możliwie najlepsze nadanie etykiet, nieoznaczonym danym z podanego zbioru." - To zdanie jest nieprawdziwe - nadawanie etykiet powinno zgodnie z implemetacją FixMatcha następować w trakcie trenowania modelu
- "Mamy więc do czynienia z dwoma niezależnymi etapami, z których każdy wymaga osobnej walidacji." - to zdanie również jest nieprawdziwe, bo nie mamy żadnych dwóch niezależnych etapów.
- Plan działania jest nieadekwatny do metod które chcą Panowie wykorzystać
- Jeśli chodzi o ewaluację to proszę skupić się na metrykach wykorzystywanych w problemie, czyli AUC lub accuracy


## AQ
- Czy jest możliwość udostępnienia zewnętrznego środowiska wykonawczego?

Jak rozumiemy problem:
- Labelowanie FixMachem
- Wykorzystanie zalabelowanych danych do klasyfikacji choroby i miejsca występowania (bouding boxy) poprzez chexnet
- Jaki baseline przyjąć? ODP: model który jest uczony na małej ilości danych, bez użycia fixmacha
- czy do walidacji użyć ground truth czy tego co da nam fixmach? Zapominamy o wymazanym ground true

Skitzo notatki z 06/05/24

uwaga może być multilabel

multiclass, jak predykcja??
Różny podział 

Bez bez dolabelowanych
14:30

Porównanie ze względu na 
3 modele
Do predykcji: jedna klasa wybrana, cutoffy, cutoffy per klasa Krzywe ROC


Do ustalenia cutoffu:
Krzywe ROC lub Precision ROC do cutoffu dane treningowe

31/05/24

- zapytać, czy sprawko ma spoko rozkład
