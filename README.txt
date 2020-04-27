.. contents::

Einführung
==========

Mit diesem Add-On werden verschiedene Behaviors für Content-Types zur Verfügung gestellt. In den folgenden Abschnitten sollen die Bedeutung
und die Funktion der Behaviors erklärt werden:


Einstellungen für die nva.kurzfassung
-------------------------------------

Die hier beschriebenen Möglichkeiten zur Konfiguration von Einstellungen wirken nur für angepasste Plone-Standard-Templates 
(z.B. Anpassung im Theme Produkt) bzw. für die Darstellungsformen des Packages nva.kurzfassung. Eine Wirkung der Einstellungen
für Standard-Plone-Ansichten ist nicht garantiert.

1. alttitle (Titel: Alternativer Titel, TextLine)
2. dachzeile (Titel: Dachzeile, TextLine) - wird oberhalb des Titels angezeigt
3. bachvalue (Titel: Anzahl der Artikel im Stapel, Choice) - es werden diverse Stapelgrößen angeboten (z.B. Ordnerinhalte)
4. excludeFromDisplay (Titel: Von Anzeige ausschließen, Bool)
5. columns (Titel: Anzahl von Spalten in der Kartenansicht)

Beispiele::

    if 'dachzeile' in context.__dict__:
        if context.dachzeile:
            dachzeile = context.dachzeile
            return dachzeile

    if 'excludeFromDisplay' in context.__dict__:
        return context.excludeFromDisplay    


Titelbild
---------

Mit diesem Behavior sollen im Kopf eines Dokuments, Ordners oder sonstigen Artikeltypen großflächige Titelbilder (Bühnenbilder)
angezeigt werden. Es handelt sich dabei um eine Liste von Referenzen (RelationList). Befindet sich in der Liste ein Bildobjekt
soll dieses als großflächiges Stand-Bühnenbild angezeigt werden. Bei einer Liste von Bildern soll eine Art von Slider aktiviert
werden. Das Behavior erweitert die Artikel um folgende Felder:

1. titleimages (Titel: Titelbilder, RelationList)
2. embedcode (Titel: Einbettungscode einer Videoplattform, Text) alternativ zum Bühnenbild kann ein großflächiges Video (16:9) eingeblendet werden.
3. viewlet (Titel: Anzeige der Titelbilder, Choice) Hier soll den Autoren eine Auswahl von Darstellungsformen für die Anzeige angeboten werden.


Ordnertexte
-----------

Der Standard-Artikeltyp Ordner wird mit diesem Behavior um 2 Richtext-Felder erweitert.

1. text (Titel: Haupttext, RichText) Dieses Feld soll oberhalb der Auflistung der Artikel im Ordner angezeigt werden.
2. schlusstext (Titel: Schlusstext, RichText) Dieses Feld soll unterhalb der Auflistung der Artikel im Ordner angezeigt werden.


Inhalte als Karten
------------------

Plone Portlets weisen diverse Nachteile auf. Beispielsweise werden die Portlet-Inhalte nicht katalogisiert. Außerdem können Portlets nicht
kopiert oder bewegt werden. Portlets stehen aus Sicht des Designs nicht im unmittelbaren Kontext eines Inhalts und sind auch nicht über
die plone.restapi erreichbar. Die Plone-Portlets sollen deshalb durch neue Lösungen ersetzt werden:

- Inhalte sollen als Karten an der Position der heutigen Portlets dargestellt werden.
- Ausserdem sollen Inhalte als Karten im Contentbereich dargestellt werden können (z.B. als Kartendeck), um z.B. mit Content-Karten auf
  weiterreichende Informationen verweisen zu können.

Das Behavior enthält 2 Referenzfelder:

1. cards (Titel: Auswahl der Portlets, RelationList)
2. contentcards (Titel: Auswahl der Content-Karteni, RelationList)

Bei einem aktivierten Behavior können die Karten mit folgenden Methoden im Kontext eines Inhaltstyps aufgerufen werden::

    cards = context.cards
    for i in cards:
        cardobj = i.to_object

    contentcards = context.contentcards
    for i in contentcards:
        cardobj = i.to_object

Aktuell können im Bereich der cards folgende Artikeltypen referenziert werden:

- Document
- Image
- Collection

Funktional soll dabei folgendes erreicht werden:

- bei einem Dokument soll der Titel des Dokuments im Portlet-Header und der Haupttext im Kartentext dargestellt werden.
- bei einem Bild soll das Bild im Portlet dargestellt werden und das Bild mit dem Verweis des Bildes verlinkt werden.
- bei einer Kollektion soll der Titel der Kollektion im Portlet-Header erscheinen und die Trefferobjekte verlinkt gelistet werden.

Die neue Art der Portlets sollen analog zu Plone-Portlets immer in der äußeren rechten Spalte dargestellt werden.
Die Content-Cards sollen in einem Kartendeck unterhalb des Haupttextes dargestellt werden.

