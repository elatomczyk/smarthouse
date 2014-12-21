# README #

Python == 2.7.6

Instalacja projektu lokalnie:

    1: Tworzymy katalog o nazwie SmarthouseV

    2: Będąc w katalogu SmarthouseV przygotowujemy wirtualne środowisko:

	virtualenv SmartHV
	source bin/activate

    3: Przechodzimy do katalogu SmartHV i pobieramy pliki projektu z repozytorium: 

	git clone git@bitbucket.org:Celina_C/smarthouse.git
	
    4: Instalujemy w środowisku potrzebne moduły. Korzystamy z pliku requirements.txt pobranego z repozytorium:

	pip install -r requirements.txt
	
Uruchamianie projektu:

    1: Przechodzimy do katalogu smarthouse

    2: Uruchamiamy serwer:

	python manage.py runserver