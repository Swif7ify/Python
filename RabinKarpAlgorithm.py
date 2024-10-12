
def rabin_karp(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                print(f"Pattern found at index {i}")

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q

            if t < 0:
                t += q

text = "Loremipsumdolorsitamet,consecteturadipiscingelit.Nullamnonodioeuenimauctormollissednonmagna.Sedvitaesempermagna.Suspendissepotenti.Fusceatipsumatarcuiaculisvulputatenecarisus.Nuncdapibuseratamaurislacinia,aclaoreetarcugravida.Etiamnecliberositametmiultricesposuere.Duisinterdumsuscipitligulaatsodales.Utnonjustoinliguladignissimmalesuadanecacnulla.Integerfeugiatvariusorci,euaccumsandolorconsecteturat.Vestibulumacvehiculaerat.Donecavariuslibero,nondictumerat.Integervehiculasemacleotempus,velaliquamloremscelerisque.Invehiculanisiatjustocursusaliquet.Nullamacorcimetus.Donecfeugiatlectusvelmagnadictumcongue.Phasellusmaximusvenenatisjustositametvolutpat.Craseuodiofelis.Nullamvehiculaeuismodjusto,eualiquamsapienvenenatiseu.Donecacmassainarcumalesuadafringillanecvelmi.Inhachabitasseplateadictumst.Inornarejustoetlaciniaullamcorper.Proinconvallisaugueegetnuncvenenatisvolutpat.Nullamsedturpisfelis.Etiamvelenimetlectusmalesuadahendreritainlorem.Maurisnecarcuidrisusaliquamlaciniaatsitametdolor.Vivamusegetauguesuscipit,sodalesorcisitamet,dignissimjusto.Namdapibuslectussitametfringillaaliquet.Suspendissenecmagnasem.Nullamvariusarcuafelisfermentum,etaliquetmilaoreet.Phasellustinciduntexlorem,sedaliquetduisuscipitin.Aliquameratvolutpat.Sedaduimalesuada,aliquetligulaac,dictumdolor.Integersuscipitlectusanequefacilisis,acrhoncusmialiquet.Utinfelissitamettortorornarevenenatisidsitametdolor.Ineuismodmetuslibero,acgravidaenimmalesuadanec.Pellentesquetinciduntligulaaligulatempor,nonvenenatislorembibendum.Proinidliberosagittis,tinciduntestin,scelerisquenisl.Maecenasornaretinciduntvelit,egetvestibulumligularutrumet.Integeramassasuscipit,bibendumlectusnon,maximuslacus.Nuncdictumvariusnunc,ettempusodiopellentesquenec.Pellentesquetinciduntexnonurnavolutpat,sedsodalesrisusgravida.Nullafacilisi.Fusceconvallislectusvitaequamconsectetur,acsodaleseratornare.Vestibuluminfelisultricies,fringillamagnaid,maximusurna.Curabituranunclibero.Phasellusnecmassaaturpisdapibusviverra.Sedluctusvehiculaorciacegestas.Integervolutpatlectusinnibhrutrumtempor.Integermaximusrisusatquamvenenatis,egetfeugiatloremcursus.###PATTERN123###Donecmalesuadafacilisislacusidefficitur.Aeneanaurnavarius,feugiatlectusnec,vehiculaipsum.Maurisactinciduntarcu,atrhoncuslacus.Donecscelerisque,nullavelaliquamtincidunt,arcusapienposuerenulla,avehiculaligulafelisatarcu.Etiamconguediaminmagnaiaculis,actinciduntliberodignissim.Nuncsitametconguedolor,atrhoncuslibero.Fuscevelligulavelenimtinciduntlaoreet.Duiseurisusaugue.Suspendissepotenti.Phasellussitametpurusfelis.Curabiturgravidavelitegetmagnabibendum,noncursuslorembibendum."
pattern = "PATTERN123"
rabin_karp(text, pattern)
