def patternMatching(text, pattern):
    txt = list(text)
    pat = list(pattern)
    i = 0
    j = 0
    while i < len(txt):
        if pat[i] == txt[j]:
            i +=1
            j +=1
        else:
            j += 1
            i = 0
        if i == len(pat):
            return j - len(pat)
    return -1


text = "Loremipsumdolorsitamet,consecteturadipiscingelit.Nullamnonodioeuenimauctormollissednonmagna.Sedvitaesempermagna.Suspendissepotenti.Fusceatipsumatarcuiaculisvulputatenecarisus.Nuncdapibuseratamaurislacinia,aclaoreetarcugravida.Etiamnecliberositametmiultricesposuere.Duisinterdumsuscipitligulaatsodales.Utnonjustoinliguladignissimmalesuadanecacnulla.Integerfeugiatvariusorci,euaccumsandolorconsecteturat.Vestibulumacvehiculaerat.Donecavariuslibero,nondictumerat.Integervehiculasemacleotempus,velaliquamloremscelerisque.Invehiculanisiatjustocursusaliquet.Nullamacorcimetus.Donecfeugiatlectusvelmagnadictumcongue.Phasellusmaximusvenenatisjustositametvolutpat.Craseuodiofelis.Nullamvehiculaeuismodjusto,eualiquamsapienvenenatiseu.Donecacmassainarcumalesuadafringillanecvelmi.Inhachabitasseplateadictumst.Inornarejustoetlaciniaullamcorper.Proinconvallisaugueegetnuncvenenatisvolutpat.Nullamsedturpisfelis.Etiamvelenimetlectusmalesuadahendreritainlorem.Maurisnecarcuidrisusaliquamlaciniaatsitametdolor.Vivamusegetauguesuscipit,sodalesorcisitamet,dignissimjusto.Namdapibuslectussitametfringillaaliquet.Suspendissenecmagnasem.Nullamvariusarcuafelisfermentum,etaliquetmilaoreet.Phasellustinciduntexlorem,sedaliquetduisuscipitin.Aliquameratvolutpat.Sedaduimalesuada,aliquetligulaac,dictumdolor.Integersuscipitlectusanequefacilisis,acrhoncusmialiquet.Utinfelissitamettortorornarevenenatisidsitametdolor.Ineuismodmetuslibero,acgravidaenimmalesuadanec.Pellentesquetinciduntligulaaligulatempor,nonvenenatislorembibendum.Proinidliberosagittis,tinciduntestin,scelerisquenisl.Maecenasornaretinciduntvelit,egetvestibulumligularutrumet.Integeramassasuscipit,bibendumlectusnon,maximuslacus.Nuncdictumvariusnunc,ettempusodiopellentesquenec.Pellentesquetinciduntexnonurnavolutpat,sedsodalesrisusgravida.Nullafacilisi.Fusceconvallislectusvitaequamconsectetur,acsodaleseratornare.Vestibuluminfelisultricies,fringillamagnaid,maximusurna.Curabituranunclibero.Phasellusnecmassaaturpisdapibusviverra.Sedluctusvehiculaorciacegestas.Integervolutpatlectusinnibhrutrumtempor.Integermaximusrisusatquamvenenatis,egetfeugiatloremcursus.###PATTERN123###Donecmalesuadafacilisislacusidefficitur.Aeneanaurnavarius,feugiatlectusnec,vehiculaipsum.Maurisactinciduntarcu,atrhoncuslacus.Donecscelerisque,nullavelaliquamtincidunt,arcusapienposuerenulla,avehiculaligulafelisatarcu.Etiamconguediaminmagnaiaculis,actinciduntliberodignissim.Nuncsitametconguedolor,atrhoncuslibero.Fuscevelligulavelenimtinciduntlaoreet.Duiseurisusaugue.Suspendissepotenti.Phasellussitametpurusfelis.Curabiturgravidavelitegetmagnabibendum,noncursuslorembibendum."
pattern = "PATTERN123"
result = patternMatching(text, pattern)
print(f"Pattern Found in index: {result}")


