def KMP_algorithm(text, pattern):
	lps = [0] * len(pattern)

	prevLPS, i = 0, 1
	while i < len(pattern):
		if pattern[i] == pattern[prevLPS]:
			lps[i] = prevLPS + 1
			prevLPS += 1
			i += 1
		elif prevLPS == 0:
			lps[i] = 0
			i += 1
		else:
			prevLPS = lps[prevLPS - 1]

	i = 0
	j = 0
	while i < len(text):
		if text[i] == pattern[j]:
			i, j = i + 1, j + 1
		else:
			if j == 0:
				i += 1
			else:
				j = lps[j - 1]
		if j == len(pattern):
			return i - len(pattern)
	return -1


text = "Loremipsumdolorsitamet,consecteturadipiscingelit.Nullamnonodioeuenimauctormollissednonmagna.Sedvitaesempermagna.Suspendissepotenti.Fusceatipsumatarcuiaculisvulputatenecarisus.Nuncdapibuseratamaurislacinia,aclaoreetarcugravida.Etiamnecliberositametmiultricesposuere.Duisinterdumsuscipitligulaatsodales.Utnonjustoinliguladignissimmalesuadanecacnulla.Integerfeugiatvariusorci,euaccumsandolorconsecteturat.Vestibulumacvehiculaerat.Donecavariuslibero,nondictumerat.Integervehiculasemacleotempus,velaliquamloremscelerisque.Invehiculanisiatjustocursusaliquet.Nullamacorcimetus.Donecfeugiatlectusvelmagnadictumcongue.Phasellusmaximusvenenatisjustositametvolutpat.Craseuodiofelis.Nullamvehiculaeuismodjusto,eualiquamsapienvenenatiseu.Donecacmassainarcumalesuadafringillanecvelmi.Inhachabitasseplateadictumst.Inornarejustoetlaciniaullamcorper.Proinconvallisaugueegetnuncvenenatisvolutpat.Nullamsedturpisfelis.Etiamvelenimetlectusmalesuadahendreritainlorem.Maurisnecarcuidrisusaliquamlaciniaatsitametdolor.Vivamusegetauguesuscipit,sodalesorcisitamet,dignissimjusto.Namdapibuslectussitametfringillaaliquet.Suspendissenecmagnasem.Nullamvariusarcuafelisfermentum,etaliquetmilaoreet.Phasellustinciduntexlorem,sedaliquetduisuscipitin.Aliquameratvolutpat.Sedaduimalesuada,aliquetligulaac,dictumdolor.Integersuscipitlectusanequefacilisis,acrhoncusmialiquet.Utinfelissitamettortorornarevenenatisidsitametdolor.Ineuismodmetuslibero,acgravidaenimmalesuadanec.Pellentesquetinciduntligulaaligulatempor,nonvenenatislorembibendum.Proinidliberosagittis,tinciduntestin,scelerisquenisl.Maecenasornaretinciduntvelit,egetvestibulumligularutrumet.Integeramassasuscipit,bibendumlectusnon,maximuslacus.Nuncdictumvariusnunc,ettempusodiopellentesquenec.Pellentesquetinciduntexnonurnavolutpat,sedsodalesrisusgravida.Nullafacilisi.Fusceconvallislectusvitaequamconsectetur,acsodaleseratornare.Vestibuluminfelisultricies,fringillamagnaid,maximusurna.Curabituranunclibero.Phasellusnecmassaaturpisdapibusviverra.Sedluctusvehiculaorciacegestas.Integervolutpatlectusinnibhrutrumtempor.Integermaximusrisusatquamvenenatis,egetfeugiatloremcursus.###PATTERN123###Donecmalesuadafacilisislacusidefficitur.Aeneanaurnavarius,feugiatlectusnec,vehiculaipsum.Maurisactinciduntarcu,atrhoncuslacus.Donecscelerisque,nullavelaliquamtincidunt,arcusapienposuerenulla,avehiculaligulafelisatarcu.Etiamconguediaminmagnaiaculis,actinciduntliberodignissim.Nuncsitametconguedolor,atrhoncuslibero.Fuscevelligulavelenimtinciduntlaoreet.Duiseurisusaugue.Suspendissepotenti.Phasellussitametpurusfelis.Curabiturgravidavelitegetmagnabibendum,noncursuslorembibendum."
pattern = "PATTERN123"
result,tmk = KMP_algorithm(text, pattern, timed)
print(f"Found Pattern at index {result}")



