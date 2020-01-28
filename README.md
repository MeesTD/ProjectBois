# Rushhour


Rush Hour is een schuifpuzzel, waarbij het doel is om de rode auto naar de uitgang te verplaatsen door andere auto's te verplaatsen en dit in zo min mogelijk stappen te doen. De auto's verschillen van oriëntatie en mogen alleen in de oorspronkelijke richting bewegen. De auto's komen voor in verschillende formaten: auto's van 2 blokjes en trucks van 3 blokjes. Ook de borden kunnen verschillen van formaten, zo bestaan er borden van 6x6, 9x9 en 12x12. 


![Bord6x6](doc/1.jpg) ![Bord9x9](doc/2.jpg) ![Bord12x12](doc/3.jpg)

### Vereisten

Voor het project hebben wij de volgende programma's gebruikt.
*[python](https://www.python.org/downloads/)<br>

### Gebruik

1. Installeer python
[mac](https://www.python.org/downloads/mac-osx/)
[windows](https://www.python.org/downloads/windows/)

2. Kloon deze repository
```sh
git clone https://github.com/MeesTD/ProjectBois
```

De verschillende algorimtes kunnen worden aangeroepen door main.py aan te roepen met het algoritme die u wenst te gebruiken.
We hebben een interface gemaakt die na het runnen van main.py vraagt:


1. Welke puzzel je wilt runnen. (Typ de grootte en nummer van de puzzel hier in)
2. Welke algoritme je wilt runnen. (Typ het over uit de lijst erboven)
3. Hoe vaak je het algoritme wilt runnen.
4. Of je debug mode (Het uitschrijven van CSV files voor je moves) aan wilt hebben staan en de filenames voor deze files.


### Structuur 
Deze lijst beschrijft alle belangrijke mappen en files van het project, en hun locaties:

* **/code**: bevat alle code van dit project.
	* **/code/algorithms**: bevat de random, breadthfirst, breadthfirst met priority queue en reverse a* algoritmes.
	* **/code/objects**: bevat de board, car, lookahead, route en rushhour objecten.
* **/data**: bevat alle csv bestanden met auto's van alle borden.
	* **/data/outputs**: Deze folder bevat alle outputs van de algorithmes. 

### Auteurs
- Mees Drissen
- Mats Pijning
- Zeno Degenkamp

### Licentie

Copyright 2019 Alle rechten voorbehouden

