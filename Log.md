Maandag 6 januari:
Wij hebben met zijn drieeën gekeken naar de case. Een kleine design doc + Powerpoint presentatie gemaakt om voor onszelf wat meer duidelijkheid te creeëren over wat we precies willen doen. Door de design doc konden we het probleem in kleinere problemen opdelen die wij op moesten lossen. Zoals: 
* We moeten een bord simuleren. : Dit gaan we doen met een matrix.
* We moeten de autootjes simuleren. : Auto's worden objecten die een naam, richting, lengte en hun coördinaten bevatten
* We moeten de autootjes linken aan het bord. : Dit gaan we doen door een lijst te maken die tussen het bord en de auto objecten instaat
* We moeten ervoor zorgen dat auto's niet door elkaar heen kunnen bewegen, of buiten het bord komen. : Dit willen we doen door continue te checken of er geen auto in de route zit als je een move maakt.
* De rode auto moet bij de uitgang komen, maar hoe laat je de computer weten dat dit is bereikt? : Dit willen we doen door te kijken wanneer de rode auto op de coördinaten staat die overeenkomen met de uitgang.
* Hoe gaan we het geheel visualiseren? : Voor nu houden we het bij een visualisatie die lijkt op mario: Veel print statements.

Dinsdag 7 januari:
Na de presentatie zijn we de matrix gaan implementeren. We hadden nog wat moeite met het precies goed initialiseren van de lijsten waar de matrix uit bestaat maar na wat werk kregen we de lijsten zo ver dat ze de matrix juist weergaven. We kwamen terug bij een probleem dat deed denken aan mario: Wanneer begin en eindig je je for-loops om de matrix op de juiste manier te creeëren? 

Woensdag 8 januari:
Vandaag hebben we 1 enkele auto op een speelveld van 3x3 weten te plaatsen met een visualisatie. De visualisatie printten we hetzelfde als de pyramide in mario. Ook hierbij liepen we tegen hetzelfde probleem als dinsdag aan: wanneer begin en eindig je for loops en wat moet op welk moment geprint worden. Na wat gepuzzel waren we hieruit gekomen.
Vervolgens hadden we 1 enkele rode auto gelinkt aan het speelveld. De coördinaten van de auto linken we aan de coördinaten van het veld door tijdens het printen te kijken wanneer de coördinaten van een auto overeenkomen met de huidige positie van het printen. We moeten er nu alleen nog voor zorgen dat we de lengten van de auto ook juist weergeven in plaats van dat iedere auto maar 1 blokje in de matrix in beslag neemt.

Donderdag 9 januari:
We zijn de dag begonnen met het netjes maken van onze repository (inclusief deze log!). De readme updaten en wat puntjes op de i zetten in onze powerpoint. Verder hebben we vandaag gewerkt aan het modulair maken van onze code. We hadden hier en daar wat files voor objects maar nu hebben we ieder object zijn eigen file gegeven in de code map en dit met elkaar verbonden. Daarnaast hebben we de repository schoongemaakt en hebben we auto's zo ver gekregen dat we ze kunnen bewegen. Nu moeten we alleen nog collision detection met andere auto's en een win condition implementeren.

Vrijdag 10 januari:
Win condition geimplementeerd. We dachten het gister gedaan te hebben maar we berekenden alleen een onderdeel van de win condition. Nu returned de functie correct de win coordinaten. Ook hebben we een begin gemaakt met collision detection. Maar hij is nog niet af

Maandag 11 januari: We hebben ons coordinaten systeem van de auto's compleet moeten omgooien omdat het niet een effectieve manier was van coordinaten bijhouden. Nu hebben we een lijst van lijsten die de coordinaten bijhoudt, eigenlijk hetzelfde als de grid. Deze runnen we tegenover de coordinaten van andere auto's per stap die gezet wordt om te zorgen dat er geen collision is. Ook hebben we gezorgd dat de auto's niet buiten de grid kunnen komen.

Dinsdag 12 januari: We hebben de eerste werkende versie van het programma en random!

