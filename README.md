# README #

Python == 2.7.6

Instalacja projektu lokalnie:

1: Tworzymy katalog o nazwie SmarthouseV

2: Będąc w katalogu SmarthouseV przygotowujemy wirtualne środowisko:

	virtualenv SmartHV

3:  Przechodzimy do katalogu SmartHV i aktywujemy środowisko virtualenv poleceniem:

	source bin/activate

4: Pobieramy pliki projektu z repozytorium: 

	git clone git@bitbucket.org:Celina_C/smarthouse.git
	
5: Przechodzimy do katalogu smarthouse i instalujemy w środowisku potrzebne moduły. Korzystamy z pliku requirements.txt pobranego z repozytorium:

	pip install -r requirements.txt
	
Uruchamianie projektu:

1: Uruchamiamy serwer:

	python manage.py runserver