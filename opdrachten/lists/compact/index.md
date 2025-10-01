# Compact

Schrijf een functie `compact` met uitgebreide doctests die een referentie naar een lijst aanneemt en een nieuwe lijst oplevert met daarin de "falsy" elementen verwijderd --- dat zijn elementen die Python min of meer gelijk stelt aan `False`, zoals `0` of `''`. Maar je gaat niet specifiek zoeken naar die waarden, want je kunt deze eigenschap testen met de formule `if not x` / `if x`. Gebruik die als filter.

De functie moet een nieuwe "gecompacteerde" lijst returnen en de oude lijst moet onveranderd blijven.

## Type

Ook bij deze functie maakt het niet uit wat het type is van de *elementen* van de lijst.

## Algoritme

Formuleer een compact algoritme waarin je gebruik maakt van de basisoperaties van Python.

Bedenk vooraf:

- wat de input is
- hoe het algoritme er globaal uit moet zien (loops, variabelen)
- wat er teruggegeven wordt en hoe je dat opbouwt (variabele)
- of er nog bijzondere gevallen zijn om rekening mee te houden

<details markdown="1"><summary markdown="span">Weet je niet waar te beginnen?</summary>
Dit zijn enkele elementen die je bij deze opdracht kunt gebruiken:

- een `for`-loop waarin je een lege lijst vult met elementen uit origineel
- alleen element overnemen als `if element`
</details>
