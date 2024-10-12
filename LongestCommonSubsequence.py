def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)

    L = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    lcs_length = L[m][n]

    index = lcs_length
    lcs = [""] * (index + 1)
    lcs[index] = ""


    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return lcs_length, ''.join(lcs)

X = "Loremipsumdolorsitamet,consecteturadipiscingelit.Nullamnonodioeuenimauctormollissednonmagna.Sedvitaesempermagna.Suspendissepotenti.Fusceatipsumatarcuiaculisvulputatenecarisus.Nuncdapibuseratamaurislacinia,aclaoreetarcugravida.Etiamnecliberositametmiultricesposuere.Duisinterdumsuscipitligulaatsodales.Utnonjustoinliguladignissimmalesuadanecacnulla.Integerfeugiatvariusorci,euaccumsandolorconsecteturat.Vestibulumacvehiculaerat.Donecavariuslibero,nondictumerat.Integervehiculasemacleotempus,velaliquamloremscelerisque.Invehiculanisiatjustocursusaliquet.Nullamacorcimetus.Donecfeugiatlectusvelmagnadictumcongue.Phasellusmaximusvenenatisjustositametvolutpat.Craseuodiofelis.Nullamvehiculaeuismodjusto,eualiquamsapienvenenatiseu.Donecacmassainarcumalesuadafringillanecvelmi.Inhachabitasseplateadictumst.Inornarejustoetlaciniaullamcorper.Proinconvallisaugueegetnuncvenenatisvolutpat.Nullamsedturpisfelis.Etiamvelenimetlectusmalesuadahendreritainlorem.Maurisnecarcuidrisusaliquamlaciniaatsitametdolor.Vivamusegetauguesuscipit,sodalesorcisitamet,dignissimjusto.Namdapibuslectussitametfringillaaliquet.Suspendissenecmagnasem.Nullamvariusarcuafelisfermentum,etaliquetmilaoreet.Phasellustinciduntexlorem,sedaliquetduisuscipitin.Aliquameratvolutpat.Sedaduimalesuada,aliquetligulaac,dictumdolor.Integersuscipitlectusanequefacilisis,acrhoncusmialiquet.Utinfelissitamettortorornarevenenatisidsitametdolor.Ineuismodmetuslibero,acgravidaenimmalesuadanec.Pellentesquetinciduntligulaaligulatempor,nonvenenatislorembibendum.Proinidliberosagittis,tinciduntestin,scelerisquenisl.Maecenasornaretinciduntvelit,egetvestibulumligularutrumet.Integeramassasuscipit,bibendumlectusnon,maximuslacus.Nuncdictumvariusnunc,ettempusodiopellentesquenec.Pellentesquetinciduntexnonurnavolutpat,sedsodalesrisusgravida.Nullafacilisi.Fusceconvallislectusvitaequamconsectetur,acsodaleseratornare.Vestibuluminfelisultricies,fringillamagnaid,maximusurna.Curabituranunclibero.Phasellusnecmassaaturpisdapibusviverra.Sedluctusvehiculaorciacegestas.Integervolutpatlectusinnibhrutrumtempor.Integermaximusrisusatquamvenenatis,egetfeugiatloremcursus.###PATTERN123###Donecmalesuadafacilisislacusidefficitur.Aeneanaurnavarius,feugiatlectusnec,vehiculaipsum.Maurisactinciduntarcu,atrhoncuslacus.Donecscelerisque,nullavelaliquamtincidunt,arcusapienposuerenulla,avehiculaligulafelisatarcu.Etiamconguediaminmagnaiaculis,actinciduntliberodignissim.Nuncsitametconguedolor,atrhoncuslibero.Fuscevelligulavelenimtinciduntlaoreet.Duiseurisusaugue.Suspendissepotenti.Phasellussitametpurusfelis.Curabiturgravidavelitegetmagnabibendum,noncursuslorembibendum."
Y = "PATTERN123"
length, lcs_string = longest_common_subsequence(X, Y)
print(f"Length of LCS: {length}")
print(f"LCS: {lcs_string}")
