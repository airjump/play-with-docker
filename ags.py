'''

Adressierung von Geraeten die durch einen Broadcast Informationen bekommen 
Stand: 31.07.2019

'''

gags = "05382072"							# Geraete AGS // Empfaenger
ags = "05382072"							# Variable Amtlicher Gemeindeschluessel; Beispiel Wachtberg


print ("AGS: " ,ags)
print ("GAGS: " ,gags)

print ("Bundesland: " ,ags[0:2])			# Bundesland
print ("Regierungsbezirks" ,ags[2:3])		# Regierungsbezirks; wenn nicht vorhanden: 0
print ("Landkreise" ,ags[3:5])				# Landkreises oder der kreisfreien Stadt
print ("Gemeinde" ,ags[5:9])				# Gemeinde

print ("Vergleich" ,gags == ags)			# Vergleich der beiden AGSen und bei True gibt das Geraet etwas aus

print ("Laenge der AGS" ,len(ags))			# Ausgabe der Lange des String in der Variable

if ags == gags :
    print("Beide AGS Nummern stimmen ueberein: ", ags," & " ,gags)
else :
    print ("Nicht gleiche: ", ags," & " ,gags)

bundesland = ags[0:2]
regierungsbezirk = ags[2:3]
landkreise = ags[3:5]
gemeinde = ags[5:9]

print ("Ausgabe:" ,bundesland ," | " ,regierungsbezirk ," | " ,landkreise ," | " , gemeinde)

if bundesland == gags[0:2] :
   print ("Bundesland stimmt ueberein")
