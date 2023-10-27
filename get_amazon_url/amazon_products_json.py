# Create an empty list to store phone dictionaries
iphone_list = []

# Define a list of phone data, where each item represents information for one phone
phone_data = [
    {
        "title": "Apple iPhone 15 (128GB) - Black",
        "url": "https://www.amazon.de/Apple-iPhone-15-128-GB/dp/B0CHXFCYCR?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2XAJYOI3TMWGO&keywords=iphone&qid=1697872688&sprefix=iphone%2Caps%2C100&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1&linkCode=ll1&tag=salesdetectiv-21&linkId=458244e37916efe4b4de6a10ddf0c57c&language=de_DE&ref_=as_li_ss_tl",
        "image": "https://m.media-amazon.com/images/I/61eEYLATF9L._AC_SX679_.jpg",
        "price": 901.55,
        "rating": 3.4,
        "total_rating": 134,
        "description": "DYNAMIC ISLAND COMES ON THE IPHONE 15 – Dynamic Island brings clues and live activities forward – so you don't miss anything when you're doing something else. See who's calling, whether your flight is on time, and more.Innovative design - The iPhone 15 has a robust design made of dyed glass and aluminium. It is protected from water and dust. The ceramic shield front is harder than any smartphone glass. And the 6,1 inch Super Retina XDR display is up to 2x brighter in the sun than that of the iPhone 14,48 MP main camera with 2 x telephoto zoom - The 48 MP main camera records in super high resolution. This makes it even easier to take incredible pictures with fantastic details. And with the 2x optical tele zoom you can achieve the perfect close-up shot.Next generation portraits – Capture portraits with significantly more detail and colours. Just tap to shift focus from one subject to another, even after shooting.With the power of the A16 Bionic Chip - The super-fast chip delivers the power for advanced features such as computation-based photography, smooth transitions in Dynamic Island and voice isolation during phone calls. And the A16 Bionic is incredibly efficient so you have battery for the whole day.USB C connectivity - With the USB C port, you can charge your Mac or iPad with the same cable as your iPhone 15. With the iPhone 15, you can even charge your Apple Watch and AirPods.Important safety features - If you need to contact an emergency service, but have no network and no WiFi, you can use emergency call SOS via satellite. 4. With accident detection, the iPhone can detect a serious car accident and call for help if you can't.MADE TO MAKE A DIFFERENCE - iPhone comes with privacy features that keep you in control of your data. It is made from more recycled materials to minimize environmental impact. And it has built-in features that make the iPhone more accessible to everyone.COMES WITH APPLECARE WARRANTY - Every iPhone comes with a one-year manufacturer warranty and up to 90 days free technical support. Get AppleCare+ or AppleCare+ with theft and loss to extend your protection."
    },
    {
        "title": "Apple iPhone 14 (128 GB) - Space Schwarz",
        "url": "https://www.amazon.de/Apple-iPhone-14-Pro-128/dp/B0BDJ61GFY?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2XAJYOI3TMWGO&keywords=iphone&qid=1697872734&sprefix=iphone%2Caps%2C100&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1&linkCode=ll1&tag=salesdetectiv-21&linkId=3b1013f85908a8400a07c36145b37bdc&language=de_DE&ref_=as_li_ss_tl",
        "image":"https://m.media-amazon.com/images/I/61XO4bORHUL._AC_SX679_.jpg",
        "price": 1079,
        "rating": 4.6,
        "total_rating": 3705,
        "description": "-6,1 inch Super Retina XDR Display mit Always On und ProMotion \n -Dynamic Island, eine magische neue Art, mit dem iPhone zu interagieren \n -48 MP Hauptkamera für bis zu 4x höhere Auflösung \n -Kinomodus jetzt in 4K Dolby Vision mit bis zu 30 fps \n  -Action Modus für ruckelfreie, frei gefilmte Videos \n -Ein wichtiges Sicherheitsfeature – die Unfallerkennung, ruft Hilfe, wenn du es nicht kannst \n -Batterielaufzeit für den ganzen Tag und bis zu 23 Stunden Videowiedergabe \n -A16 Bionic, der ultimative Smartphone Chip. Ultraschneller 5G Mobilfunk. \n                         -Branchenführende Features für Haltbarkeit wie Ceramic Shield und Wasserschutz \n -iOS 16 gibt dir noch mehr Möglichkeiten zum Personalisieren, Kommunizieren und Teilen"
    },
    {
        "title": "Apple iPhone 13 (128 GB) - Mitternacht",
        "url": "https://www.amazon.de/Apple-iPhone-13-128-GB-Mitternacht/dp/B09G9HWQYT?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=22465R70TYTM9&keywords=iphone+13&qid=1697873558&sprefix=iphone+13%2Caps%2C134&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1&linkCode=ll1&tag=salesdetectiv-21&linkId=6c5c2f517ce96d9245f9b320f3013ca0&language=de_DE&ref_=as_li_ss_tl",
        "image":"https://m.media-amazon.com/images/I/616dWFinzLL._AC_SX679_.jpg",
        "price": 706,
        "rating": 4.7,
        "total_rating": 3680,
        "description": "6,1 inch Super Retina XDR Display \n Der Kinomodus fügt automatisch geringe Tiefenschärfe hinzu und verschiebt den Fokus in deinen Videos \n Fortschrittliches Zwei-Kamera-System mit 12 MP Weitwinkel‑ und Ultraweitwinkel-Objektiven; Fotografische Stile, Smart HDR 4, Nachtmodus, 4K HDR Aufnahme mit Dolby Vision \n 12 MP TrueDepth Frontkamera mit Nachtmodus, 4K HDR Aufnahme mit Dolby Vision \n A15 Bionic Chip für superschnelle Performance \n Bis zu 19 Std. Videowiedergabe \n Robustes Design mit Ceramic Shield \n Branchenführender IP68 Wasserschutz \n "
                       "5G für superschnelle Downloads und Streaming in höchster Qualität \n iOS 15 ist vollgepackt mit neuen Features, damit du mehr mit dem iPhone machen kannst als je zuvor"

    },
    {
        "title": "Apple iPhone 15 Plus (128 GB) - Schwarz",
        "url": "https://www.amazon.de/Apple-iPhone-15-Plus-128/dp/B0CHX3ZTJQ?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1PXJEYG2BFDKX&keywords=iphone+15+pro&qid=1697873912&sprefix=iphone+15+pro+%2Caps%2C100&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1&linkCode=ll1&tag=salesdetectiv-21&linkId=0899759a7cdb84f49a935427434f2435&language=de_DE&ref_=as_li_ss_tl",
        "image":"https://m.media-amazon.com/images/I/713xdJGERML._AC_SX679_.jpg",
        "price": 1099,
        "rating": 4.6 ,
        "total_rating": 49 ,
        "description": "DIE DYNAMIC ISLAND KOMMT AUF DAS IPHONE 15 PLUS – Die Dynamic Island bringt Hinweise und Live Aktivitäten nach vorne – so verpasst du nichts mehr, wenn du gerade etwas anderes machst. Du siehst, wer anruft, ob dein Flug pünktlich ist und noch viel mehr. \n "
                        "INNOVATIVES DESIGN – Das iPhone 15 Plus hat ein robustes Design aus durchgefärbtem Glas und Aluminium. Es ist vor Wasser und Staub geschützt. Die Ceramic Shield Vorderseite ist härter als jedes Smartphone Glas. Und das 6,7 \n" 
                        "48 MP HAUPTKAMERA MIT 2X TELE ZOOM – Die 48 MP Hauptkamera nimmt in superhoher Auflösung auf. So machst du noch einfacher unglaubliche Bilder mit fantastischen Details. Und mit dem 2x Tele Zoom in optischer Qualität gelingt dir die perfekte Nahaufnahme. \n "
                        "PORTRÄTS DER NÄCHSTEN GENERATION – Nimm Porträts mit deutlich mehr Details und Farben auf. Tippe einfach, um den Fokus von einem Motiv auf ein anderes zu verschieben – sogar noch nach der Aufnahme. \n "
                        "MIT DER POWER DES A16 BIONIC CHIP – Der superschnelle Chip liefert die Power für fortschrittliche Features wie rechenbasierte Fotografie, flüssige Übergänge in der Dynamic Island und Stimmisolation bei Telefongesprächen. Und der A16 Bionic ist unglaublich effizient, damit du Batterie für den ganzen Tag hast. \n "
                        "USB C KONNEKTIVITÄT – Mit dem USB C Anschluss kannst du deinen Mac oder das iPad mit dem-sel¬ben Kabel laden wie dein iPhone 15 Plus. Mit dem iPhone 15 Plus lassen sich sogar deine Apple Watch und deine AirPods aufladen.\n "
                        "WICHTIGE SICHERHEITSFEATURES – Wenn du einen Notdienst kontaktieren musst, aber kein Netz und kein WLAN hast, kannst du Notruf SOS über Satellit nutzen. Mit der Unfallerkennung kann das iPhone einen schweren Autounfall erkennen und Hilfe rufen, wenn du es nicht kannst.\n "
                        "GEMACHT, UM EINEN UNTERSCHIED ZU MACHEN – Das iPhone kommt mit Datenschutzfeatures, die dafür sorgen, dass du die Kontrolle über deine Daten behältst. Es besteht aus mehr recycelten Materialien, um die Umweltauswirkungen zu minimieren. Und es hat integrierte Features, die das iPhone für alle zugänglicher machen.\n "
                        "KOMMT MIT APPLECARE GARANTIE – Jedes iPhone kommt mit einer einjährigen Herstellergarantie und bis zu 90 Tagen kostenlosem technischen Support. Hol dir AppleCare+ oder AppleCare+ mit Diebstahl und Verlust, um deinen Schutz zu verlängern.\n "
    },
    {---
        "title": "Apple iPhone 13 mini Plus (128GB) - Mitternacht",
        "url": "https://www.amazon.de/Apple-iPhone-Mini-128-GB-Mitternacht/dp/B09G9GH7KC?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=ME1LXK8F05B6&keywords=iphone+13+mini&qid=1697874389&sprefix=iphone+13+mini%2Caps%2C126&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1&linkCode=ll1&tag=salesdetectiv-21&linkId=80fd7653522aa914dfb513ed8e565899&language=de_DE&ref_=as_li_ss_tl",
        "image":"https://m.media-amazon.com/images/I/61zqwVNO-sL._AC_SX679_.jpg",
        "price": 724.48,
        "rating": 4.7,
        "total_rating": 3683,
        "description": "5,4 inch Super Retina XDR Display \n"
                        "Der Kinomodus fügt automatisch geringe Tiefenschärfe hinzu und verschiebt den Fokus in deinen Videos \n"
                        "Fortschrittliches Zwei-Kamera-System mit 12 MP Weitwinkel‑ und Ultraweitwinkel-Objektiven; Fotografische Stile, Smart HDR 4, Nachtmodus, 4K HDR Aufnahme mit Dolby Vision\n"
                        "12 MP TrueDepth Frontkamera mit Nachtmodus, 4K HDR Aufnahme mit Dolby Vision \n"
                        "A15 Bionic Chip für superschnelle Performance \n"
                        "Bis zu 17 Std. Videowiedergabe \n"
                        "Robustes Design mit Ceramic Shield \n"
                        "Branchenführender IP68 Wasserschutz \n"
                        "5G für superschnelle Downloads und Streaming in höchster Qualität\n"
                        "iOS 15 ist vollgepackt mit neuen Features, damit du mehr mit dem iPhone machen kannst als je zuvor\n"
    },
    {
        "title": "Apple iPhone 12",
        "url": "https://www.amazon.de/-/en/MGJF3ZD-A-Apple-iPhone-12/dp/B08L5TSDFV/ref=sr_1_7?crid=20KEBQ7N1EWQP&keywords=iphone&qid=1697733045&sprefix=iph%2Caps%2C437&sr=8-7",
        "image":"https://m.media-amazon.com/images/I/71DZ0Ue6HvL._AC_SX679_.jpg",
        "price": 730.63,
        "rating": 4.7,
        "total_rating": 9059,
        "description": "6,1 inch Super Retina XDR display (15,5 cm diagonal). Ceramic shield that can withstand more than any smartphone glass. 5G for super-fast downloads and streaming of the highest quality. A14 Bionic, the fastest chip in a smartphone. Advanced Dual Camera System with 12MP Ultra Wide Angle and Wide Angle Lens, Night Mode, Deep Fusion, Smart HDR 3, 4K Dolby Vision HDR Recording. 12MP TrueDepth Front Camera with Night Mode, 4K Dolby Vision HDR Recording. Industry-leading IP68 water protection. Supports MagSafe accessories for easy docking and faster wireless charging. iOS with new widgets on the home screen, the new app media library, app clips and more."
    },
    {
        "title": "Apple iPhone 15 Pro (512GB) - Titanium Black",
        "url": "https://www.amazon.de/-/en/Apple-iPhone-15-Pro-512GB/dp/B0CHWRZNBK/ref=sr_1_8?crid=20KEBQ7N1EWQP&keywords=iphone&qid=1697733045&sprefix=iph%2Caps%2C437&sr=8-8",
        "image":"https://m.media-amazon.com/images/I/812oGW3LDdL._AC_SX679_.jpg",
        "price": 1579,
        "rating": 4.5,
        "total_rating": 125,
        "description": "Forged from titanium - The iPhone 15 Pro has a robust and lightweight design made of space grade titanium with a textured matte glass back. It also has a ceramic shield front that can withstand more than any smartphone glass. And it is protected from water and dust. Advanced display – The 6,1 inch Super Retina XDR display with ProMotion increases refresh rates up to 120 Hz when you need a lot of graphics power. Dynamic Island brings notifications and live activities forward. And with the Always On Display, the lock screen always shows your most important information without having to tap it. ALL CHANGING A17 PRO CHIP – A Pro GPU makes games an immersive experience, with detailed environments and realistic characters. The A17 Pro is incredibly efficient and ensures that you have battery for the whole day. POWERFUL PRO CAMERA SYSTEM - Incredible flexibility in choosing the image section, as if you had 7 Pro lenses. Take super-high-resolution photos with more colour and detail with the 48MP main camera. And with the 3x Tele camera in the iPhone 15 Pro, you can take razor-sharp close-up shots from a greater distance. Customizable action button - The action button takes you directly to your favourite feature. Simply set mute mode, camera, voice memo, shortcut or other feature. Then all you have to do is press and hold the Action Button to start it. Pro connectivity - With the USB C port, you can charge your Mac or iPad with the same cable as your iPhone 15 Pro. With USB 3, you get a huge leap in data transfer. And you can load files up to 2x faster with Wi-Fi 6E. Important safety features - If you need to contact an emergency service but have no network and no WiFi, you can use emergency call SOS via satellite. With accident detection, the iPhone can detect a serious car accident and call for help when you can't. MADE TO MAKE A DIFFERENCE - iPhone comes with privacy features that keep you in control of your data. It is made from more recycled materials to minimise environmental impact. And it has built-in features that make the iPhone more accessible to everyone. COMES WITH APPLECARE WARRANTY - Every iPhone comes with a one-year manufacturer warranty and up to 90 days free technical support. Get AppleCare+ or AppleCare+ with theft and loss to extend your protection."
    },
    {
        "title": "Apple iPhone 14 Pro Max (1 TB) - Space Schwarz",
        "url": "https://www.amazon.de/-/en/MQC23ZD-A/dp/B0BDJ8G62P/ref=sr_1_10?crid=20KEBQ7N1EWQP&keywords=iphone&qid=1697733045&sprefix=iph%2Caps%2C437&sr=8-10",
        "image":"https://m.media-amazon.com/images/I/610pghkO81L._AC_SX679_.jpg",
        "price": 1952.98,
        "rating": 4.7,
        "total_rating": 3687,
        "description": "6,7 inch Super Retina XDR Display mit Always On und ProMotion. Dynamic Island, eine magische neue Art, mit dem iPhone zu interagieren. 48 MP Hauptkamera für bis zu 4x höhere Auflösung. Kinomodus jetzt in 4K Dolby Vision mit bis zu 30 fps. Action Modus für ruckelfreie, frei gefilmte Videos. Ein wichtiges Sicherheitsfeature – die Unfallerkennung, ruft Hilfe, wenn du es nicht kannst. Batterielaufzeit für den ganzen Tag und bis zu 29 Stunden Videowiedergabe. A16 Bionic, der ultimative Smartphone Chip. Ultraschneller 5G Mobilfunk. Branchenführende Features für Haltbarkeit wie Ceramic Shield und Wasserschutz. iOS 16 gibt dir noch mehr Möglichkeiten zum Personalisieren, Kommunizieren und Teilen"
    },
    {
        "title": "Apple iPhone 14 (256 GB) - Polarstern",
        "url": "https://www.amazon.de/-/en/MPW43ZD-A/dp/B0BDJJSRX6/ref=sr_1_12?crid=20KEBQ7N1EWQP&keywords=iphone&qid=1697733045&sprefix=iph%2Caps%2C437&sr=8-12",
        "image":"https://m.media-amazon.com/images/I/618Bb+QzCmL._AC_SX679_.jpg",
        "price": 908.44,
        "rating": 4.6,
        "total_rating": 3911,
        "description": "6,1 inch Super Retina XDR Display. Batterielaufzeit für den ganzen Tag und bis zu 20 Std, Videowiedergabe. Branchenführende Features für Langlebigkeit wie Ceramic Shield und Wasserschutz. A15 Bionic Chip mit 5-Core GPU für superschnelle Performance. Superschneller 5G Mobilfunk. Fortschrittliches Kamera-System für bessere Fotos bei jedem Licht. Action Modus für ruckelfreie, handgefilmte Videos. Kinomodus jetzt in 4K Dolby Vision mit bis zu 30 fps. Wichtige Sicherheitsfeatures – Notruf SOS über Satellit und Unfallerkennung. iOS 16 gibt dir noch mehr Möglichkeiten zum Personalisieren, Kommunizieren und Teilen."
    },
    {
        "title": "Apple 2022 iPhone SE (128 GB) - Mitternachtsblau (3. Generation)",
        "url": "https://www.amazon.de/-/en/MMXJ3/dp/B09V3K2RG2/ref=sr_1_11?crid=20KEBQ7N1EWQP&keywords=iphone&qid=1697738244&sprefix=iph%2Caps%2C437&sr=8-11",
        "image":"https://m.media-amazon.com/images/I/61TOWf11+jL._AC_SX679_.jpg",
        "price":599 ,
        "rating": 4.6,
        "total_rating": 599,
        "description": "4.7 inch Retina HD display (11.94 cm diagonal). Advanced one-camera system with 12MP wide-angle camera, Smart HDR 4, photographic styles, portrait mode and 4K video up to 60fps. 7MP FaceTime HD camera with Smart HDR 4, photographic styles, portrait mode and 1080p video recording. A15 Bionic chip for super-fast performance. 2 up to 15 hours of video playback. 5G mobile radio. 4 robust design and IP67 water protection. Home button with touch ID for secure authentication. iOS 15 is packed with new features so you can do more with the iPhone than"
    }
]

# Loop through the phone data and add each phone dictionary to the list
for phone in phone_data:
    a =


# Create an empty list to store gaming console dictionaries
gaming_consoles = []

# Define a list of gaming console data, where each item represents information for one console
gaming_console_data = [
   {
        "title": "Xbox Series S",
        "url": "https://www.amazon.de/-/en/RRS-00009/dp/B087VM5XC6/ref=sr_1_3?crid=1ILS9E5L3335E&keywords=gaming%2Bconsoles&qid=1697738636&sprefix=Gaming%2Bconsoles%2Caps%2C274&sr=8-3&th=1",
        "image":"https://m.media-amazon.com/images/I/31HZ6NAFIcL._SX300_SY300_QL70_ML2_.jpg",
        "price": 222,
        "rating": 4.7,
        "total_rating": 15024,
        "description": "Die kompakteste und schlankeste Xbox-Konsole aller Zeiten. Mit der kompaktesten Xbox aller Zeiten können Sie Spiele der nächsten Generation vollständig digital genießen. Bundle enthält: Xbox Series S-Konsole, einen Xbox Wireless Controller, ein Hochgeschwindigkeits-HDMI-Kabel und ein Stromkabel. Erleben Sie Next-Gen Geschwindigkeit und Leistung mit der Xbox Velocity Architecture, die von einer eigens entwickelten SSD und integrierter Software angetrieben wird. Spielen Sie dank Abwärtskompatibilität Tausende von digitalen Spielen aus vier Xbox-Generationen, einschließlich optimierter Titel bei der Markteinführung. Xbox Game Pass Ultimate umfasst über 100 großartige Spiele für Konsolen, PCs und Android-Mobilgeräte, Online-Multiplayer und eine EA Play-Mitgliedschaft zu einem niedrigen monatlichen Preis (Mitgliedschaft separat erhältlich)"
    },
    {
        "title": "Playstation 5 Standard Konsole",
        "url": "https://www.amazon.de/-/en/CFI-1216A/dp/B08H93ZRK9/ref=sr_1_4?crid=1ILS9E5L3335E&keywords=gaming+consoles&qid=1697738636&sprefix=Gaming+consoles%2Caps%2C274&sr=8-4",
        "image":"https://m.media-amazon.com/images/I/61CELS-zAZL._SX522_.jpg",
        "price": 533,
        "rating": 4.8,
        "total_rating": 21860,
        "description": "Tempest 3D AudioTech-Technologie für außergewöhnliches Eintauchen in den Sound, haptisches Feedback und adaptive Trigger über den DualSense-Controller, um die Auswirkungen und Auswirkungen Ihrer Aktionen im Spiel zu spüren (bei einer Auswahl von PS5-Spielen). Lieferumfang: 1 x Sony PlayStation 5 Konsole, 1 x DualSense Controller, 1 x Basis, Anschlüsse: 1 HDMI 2.1 Port, 3 USB Ports, 1 USB-C Port, 1 Ethernet Port, Konsolenabmessungen (BxHxL): 390 mm x 104 mm x 260 mm (ohne Ständer), Gewicht: 4,5 kg, Farbe: Weiß. Nahezu sofortige Ladezeiten für PS5-Spiele (installiert) dank eines Ultra-High-Speed-Solid-State-Laufwerks. Die Benutzeroberfläche wurde entwickelt, um sofortigen Zugriff auf fast alle Systemoptionen zu bieten, ohne das Spiel zu verlassen. Unübertroffener Realismus dank Ray Tracing Light Rendering-Technologie, Unterstützung der HDR-Technologie für lebendige und dynamische Farben, Möglichkeit, in 4K und 8K auf kompatiblen Spielen und Displays zu spielen. Nutze die Leistung der speziell entwickelten CPU, GPU und SSD mit integriertem I/O und erlebe, wie diese PlayStation-Konsole die Gaming-Welt revolutioniert. Freue dich auf blitzschnelles Laden mit einer ultraschnellen SSD, eine realistischere Spielerfahrung durch haptisches Feedback, adaptive Trigger-Tasten und 3D-Audio sowie eine völlig neue Generation unglaublicher PlayStation-Spiele."
    },
    {
        "title": "Microsoft Xbox One X 1TB Console, Black, Standard Edition",
        "url": "https://www.amazon.de/-/en/Microsoft-Xbox-Console-Black-Standard/dp/B06Y36MK86/ref=sr_1_23?crid=1ILS9E5L3335E&keywords=gaming+consoles&qid=1697738705&sprefix=Gaming+consoles%2Caps%2C274&sr=8-23",
        "image":"https://m.media-amazon.com/images/I/51ilsGij0KL._AC_SX569_.jpg",
        "price": 229.99,
        "rating": 4.4,
        "total_rating": 1128,
        "description": "Play over 1,300 great games, including current blockbusters, 200 console-exclusive titles, and 400 Xbox classics. Enjoy true 4K gaming, 4K video streaming and a 4K Blu-ray player. Play with friends on Xbox Live, the fastest and most reliable gaming network. Your Xbox One games and accessories are compatible. Bring your games and movies to life with immersive audio via Dolby Atmos and DTS:X. Includes: Xbox One X 1TB Console, Xbox Wireless Controller, 4K HDMI Cable & Power Cable, 1 Month Xbox Game Pass Trial Membership, 14-Day Xbox Live Gold Trial Membership."
    },
    {
        "title": "Xbox Series S + Starfield Standard Edition| Xbox & Windows 10/11 - Download Code",
        "url": "https://www.amazon.de/-/en/dp/B0CDQD92ZM/ref=sr_1_28?crid=1ILS9E5L3335E&keywords=gaming%2Bconsoles&qid=1697738705&sprefix=Gaming%2Bconsoles%2Caps%2C274&sr=8-28&th=1",
        "image":"https://m.media-amazon.com/images/I/712KmOYyE6L._SX466_.jpg",
        "price": 359.98,
        "rating": 4.7,
        "total_rating": 15024,
        "description": "Das Bundle besteht aus: Xbox Series S und Starfield Standard Edition (Spielbar ab 6. September). Der Download-Code wird bis zu 4 Stunden nach dem Veröffentlichungsdatum in deiner Software-Bibliothek verfügbar sein. Nutze jede Gaming-Minute optimal – dank Quick Resume, blitzschneller Ladezeiten und Gameplay mit bis zu 120 FPS – alles unterstützt von der Xbox Velocity-Architektur. Erlebe Spiele aus vier Xbox-Generationen dank Hunderter optimierter Titel, die besser aussehen und sich besser spielen lassen als je zuvor. Xbox Smart Delivery stellt sicher, dass du die beste verfügbare Version deines Spiels spielst, unabhängig davon, auf welcher Konsole du spielst. Minimiere Ladezeiten und steigere die Bildfrequenzen mit einer individuell entwickelten NVMe-SSD, damit größere, robustere Spiele mit voller Kapazität laufen. Erwecke deine Spiele und Filme mit hoher Qualität zum Leben mit einer satten, dynamischen Soundumgebung. Trete Xbox Game Pass Ultimate bei (die Mitgliedschaft ist separat erhältlich), um neue Spiele von Xbox Game Studios, Bethesda Softworks und mehr gleich ab Release zu spielen. Außerdem kannst du Hunderte Xbox-Spiele mit deinem Freundeskreis auf Konsole, PC und in der Cloud genießen. Starfield - In diesem Next-Gen-RPG von den preisgekrönten Machern von The Elder Scrolls V: Skyrim und Fallout 4 reist du zu den Sternen. Die Premium Edition enthält: Starfield-Hauptspiel, Shattered Space-Story-Erweiterung (sobald veröffentlicht), bis zu 5 Tage Early Access, Constellation-Skin-Paket: Equinox-Lasergewehr, -Anzug, -Helm und -Boostpack, Zugriff auf Starfield Digitales Artbook & Original-Soundtrack. Erstelle dir einen Charakter ganz nach deiner Vorstellung und erkunde in beispielloser Freiheit die endlosen Weiten."
    },
    {
        "title": "Xbox Series X – Starfield Standard Edition Bundle Windows 10/11 - Download Code",
        "url": "https://www.amazon.de/-/en/dp/B0CDQBDP14/ref=sr_1_6?crid=1T51EMDSY6QO0&keywords=xbox&qid=1697740074&sprefix=xbox%2Caps%2C343&sr=8-6",
        "image":"https://m.media-amazon.com/images/I/61BVvNo8E-L._SX466_.jpg",
        "price": 588.99,
        "rating":4.8 ,
        "total_rating": 14350,
        "description": "Xbox Series X ist die schnellste und leistungsstärkste Konsole aller Zeiten. Genießen Sie Tausende Spiele aus vier Konsolengenerationen, die sich nie besser gespielt haben als auf Xbox Series X. Das Herzstück der Xbox Series X ist die Xbox Velocity Architecture, die eine speziell entwickelte SSD und Software vereint und Spielwelten in Sekundenschnelle lädt. Spielen Sie durch Abwärtskompatibilität Tausende von Titeln aus vier Konsolengenerationen darunter Xbox One, Xbox 360, und Original Xbox Titel. Starten Sie durch mit Xbox Game Pass Ultimate und erhalten Sie Zugriff auf über 100 großartige Spiele, eine EA Play-Mitgliedschaft, Online-Multiplayer und alle neuen Xbox Game Studios-Titel am Tag ihrer Veröffentlichung (Mitgliedschaft separat erhältlich, EA Play ab Ende 2020 enthalten). Xbox Smart Delivery stellt sicher, dass Sie die beste Version Ihres Spiels spielen, egal, auf welcher Konsole Sie spielen."
    },
    {
        "title": "Xbox Series S 1TB Black + Starfield Standard Edition Windows 10/11 - Download Code",
        "url": "https://www.amazon.de/-/en/dp/B0CDQC2N8V/ref=sr_1_13?crid=1T51EMDSY6QO0&keywords=xbox&qid=1697740074&sprefix=xbox%2Caps%2C343&sr=8-13",
        "image":"https://m.media-amazon.com/images/I/71UHKsrC4DL._SX466_.jpg",
        "price":429.98 ,
        "rating": 4.4,
        "total_rating": 35,
        "description": "Das Bundle besteht aus: Xbox Series S 1TB Black und Starfield Standard Edition (Spielbar ab 6. September). Der Download-Code wird bis zu 4 Stunden nach dem Veröffentlichungsdatum in deiner Software-Bibliothek verfügbar sein. Nutze jede Gaming-Minute optimal – dank Quick Resume, blitzschneller Ladezeiten und Gameplay mit bis zu 120 FPS – alles unterstützt von der Xbox Velocity-Architektur. Erlebe Spiele aus vier Xbox-Generationen dank Hunderter optimierter Titel, die besser aussehen und sich besser spielen lassen als je zuvor. Xbox Smart Delivery stellt sicher, dass du die beste verfügbare Version deines Spiels spielst, unabhängig davon, auf welcher Konsole du spielst. Minimiere Ladezeiten und steigere die Bildfrequenzen mit einer individuell entwickelten NVMe-SSD, damit größere, robustere Spiele mit voller Kapazität laufen. Erwecke deine Spiele und Filme mit hoher Qualität zum Leben mit einer satten, dynamischen Soundumgebung. Trete Xbox Game Pass Ultimate bei (die Mitgliedschaft ist separat erhältlich), um neue Spiele von Xbox Game Studios, Bethesda Softworks und mehr gleich ab Release zu spielen. Außerdem kannst du Hunderte Xbox-Spiele mit deinem Freundeskreis auf Konsole, PC und in der Cloud genießen. Starfield - In diesem Next-Gen-RPG von den preisgekrönten Machern von The Elder Scrolls V: Skyrim und Fallout 4 reist du zu den Sternen. Die Premium Edition enthält: Starfield-Hauptspiel, Shattered Space-Story-Erweiterung (sobald veröffentlicht), bis zu 5 Tage Early Access, Constellation-Skin-Paket: Equinox-Lasergewehr, -Anzug, -Helm und -Boostpack, Zugriff auf Starfield Digitales Artbook & Original-Soundtrack. Erstelle dir einen Charakter ganz nach deiner Vorstellung und erkunde in beispielloser Freiheit die endlosen Weiten."
    },
    {
        "title": "Xbox One S 500GB Konsole",
        "url": "https://www.amazon.de/-/en/ZQ9-00011/dp/B01M5G69L9/ref=sr_1_15?crid=1T51EMDSY6QO0&keywords=xbox&qid=1697740074&sprefix=xbox%2Caps%2C343&sr=8-15",
        "image":"https://m.media-amazon.com/images/I/6125o51OKrL._SX522_.jpg",
        "price": 149.99,
        "rating": 4.3,
        "total_rating": 332,
        "description": "Xbox One S 500 GB Konsole & 14-tägige Xbox Live-Gold Mitgliedschaft. Neuer Xbox Wireless Controller (3,5mm Klinkenstecker, Bluetooth, Textured Grip). 4K-HDMI-Kabel & Stromkabel. Adapter. Benutzerhandbuch. mit EU-Stecker für den Einsatz in Deutschland konzipiert."
    },
    {
        "title": "PlayStation 4 - Konsole (500GB, schwarz,slim) [CUH-2016A]",
        "url": "https://www.amazon.de/-/en/711719845454/dp/B01LQF9RDI/ref=sr_1_11?crid=OXFZX3ZLCQ05&keywords=playstation&qid=1697740756&sprefix=playstatio%2Caps%2C326&sr=8-11",
        "image":"https://m.media-amazon.com/images/I/51x2uufH6SL._SX522_.jpg",
        "price": 287.97,
        "rating": 4.5,
        "total_rating": 2715,
        "description": "Festplatte: 500 GB. Grafikchip: 1.84 TFLOPS, AMD next-generation Radeon. Prozessor: x86-64 AMD 'Jaguar', 8 cores. Speicher: 8.192 MB. PlayStation Plus-Mitglieder können jährlich 24 ausgewählte PS4-Spiele ohne zusätzliche Kosten herunterladen. Mitglieder können jeden Monat neue Titel entdecken und in spannende Welten eintauchen – mit PlayStation Plus gibt es immer etwas zu spielen. Der Vertikaler Standfuß für die PlayStation 4 Konsole ist nicht im Lieferumfang enthalten."
    },
    {
        "title": "PlayStation 4 Pro - Konsole (1 TB, schwarz, Pro, Modell: CUH-7216B)",
        "url": "https://www.amazon.de/-/en/9752316/dp/B07HSJW7HK/ref=sr_1_14?crid=OXFZX3ZLCQ05&keywords=playstation&qid=1697740756&sprefix=playstatio%2Caps%2C326&sr=8-14",
        "image":"https://m.media-amazon.com/images/I/71GWJXGeZsL._AC_SX569_.jpg",
        "price": 259.99,
        "rating": 4.5,
        "total_rating": 4076,
        "description": "Inhalt: PlayStation4 Pro-System 1 Terabyte, DUALSHOCK4 Wireless-Controller , Mono-Headset, HDMI-Kabel, Netzkabel, USB-Kabel und Bedienungsanleitung. 4K-Gaming: Spiel die neuesten Spiele in gestochen scharfem 4K. Hauttöne wirken wärmer, Materialien erhalten eine realistische Struktur und Umgebungen erwachen wie nie zuvor zum Leben. Spektakuläre Grafik: Mit PS4 Pro werden Gesichtszüge realistisch dargestellt, sodass die Personen zum Leben erwachen. Kurven sind weicher und Kanten schärfer, wodurch visuelle Elemente wie Haare, Wasser und Gras ebenfalls lebendig wirken. HDR-Technologie: Mit einem HDR-Fernseher erlebst du bei kompatiblen PS4-Spielen ein unglaubliches Farbspektrum, das noch mehr dem entspricht, was das menschliche Auge in der realen Welt sieht. So entstehen beeindruckend lebendige Bilder und realistische Details. Atemberaubende Umgebungen: PS4 Pro ermöglicht eine noch genauere Darstellung von strukturellen Details wie Schmutz oder Rost in Nahaufnahmen, während dunkle, klare Schattierungen in großer Entfernung Spielen auf PS4 Pro eine unglaubliche Tiefenwirkung verleihen. Framerate-Boost: Die schnelleren und stabileren Bildwiederholungsraten sorgen dafür, dass die Action noch schneller, nahtloser und explosiver wiedergegeben wird. Unglaubliches Entertainment: Stream die besten Filme, beliebtesten TV-Serien und neuesten Videos in 4K-Auflösung von Netflix, YouTube und vielen anderen demnächst verfügbaren Entertainment-Apps – natürlich immer mit automatischem Upscaling für die bestmögliche Bildqualität."
    },
    {
        "title": "PlayStation 4 Pro - Konsole (1TB)",
        "url": "https://www.amazon.de/-/en/RED223926/dp/B01LQF9UKS/ref=sr_1_13?crid=OXFZX3ZLCQ05&keywords=playstation&qid=1697740756&sprefix=playstatio%2Caps%2C326&sr=8-13",
        "image":"https://m.media-amazon.com/images/I/41MIK16+Q5S._SX522_.jpg",
        "price": 219.99,
        "rating": 4.4,
        "total_rating": 2352,
        "description": "Dank der zusätzlichen Power unter der Haube erwachen Spiele mit packenden Grafiken und unglaublich authentischen Details zum Leben. PlayStation Plus-Mitglieder können jährlich 24 ausgewählte PS4-Spiele ohne zusätzliche Kosten herunterladen. Mitglieder können jeden Monat neue Titel entdecken und in spannende Welten eintauchen – mit PlayStation Plus gibt es immer etwas zu spielen."
    }
]
# Loop through the gaming console data and add each console dictionary to the list
for console in gaming_console_data:
    gaming_consoles.append(console)


# Create an empty list to store television dictionaries
televisions = []

television_data = [
    {
        "title": "Samsung QLED 4K Q70C 75 Inch TV + Xbox Series S - Gilded Hunter Bundle + 9 Months Game Pass Ultimate",
        "url": "https://amzn.eu/d/8kRS3ux",
        "image":"https://m.media-amazon.com/images/I/71Vu3JLnGPL._AC_SL1500_.jpg",
        "price": 2213.96,
        "rating": 4.4,
        "total_rating": 263,
        "description": "The Quantum processor 4K of the TV can improve image, sound and function using artificial intelligence. With Motion Xcelerator Turbo+ smooth movement image display when gaming in 4K/120Hz quality on the Samsung TV.Get ready to go with the Xbox Series S -Gilded Hunter Bundle, which includes nine in-game items and virtual currency for Fortnite, Rocket League and Fall Guys. With the Xbox Series S, you can experience the next generation speed and performance at an affordable price. With your active subscription to Xbox Game Pass Ultimate, you can play games on Xbox One, Xbox Series X, and Windows 10 PC. Includes console game subscription with Xbox Game Pass, subscription to PC games with Xbox Game Pass, EA Play and Xbox Live Gold."
    },
    {
        "title": "Samsung Neo QLED 4K QN85C 55 Inch TV + 2 x Xbox Wireless Controller Carbon Black + 9 Months Game Pass Ultimate",
        "url": "https://amzn.eu/d/2y9wOjV",
        "image":"https://m.media-amazon.com/images/I/91f7Qqr-zrL._AC_SL1500_.jpg",
        "price": 1477.39,
        "rating": 4.4,
        "total_rating": 332,
        "description": "Enjoy spectacular contrasts and impressive details on the Samsung TV with Neo Quantum HDR. Neural Quantum processor 4K provides a stunning TV viewing experience with AI and 20 neural networks. Experience the modernized design of the Xbox Wireless Controller in Carbon Black, with its moulded surfaces and refined geometry for more comfort while gaming. Stay on target course thanks to the textured grip surface and hybrid D pad. You can customize the controller to your needs and assign the buttons as you like via the Xbox Accessories app. With your active subscription to Xbox Game Pass Ultimate, you can play games on Xbox One, Xbox Series X, and Windows 10 PC. Includes subscription to console games with Xbox Game Pass, subscription to PC games with Xbox Game Pass, EA Play and Xbox Live Gold."
    },
    {
        "title": "LG OLED55C37LA TV 139 cm (55 Inches) + Xbox Series S with Free Content",
        "url": "https://amzn.eu/d/gzmC1pk",
        "image":"https://m.media-amazon.com/images/I/71lzaekEG5L._AC_SL1500_.jpg",
        "price": 1828.99,
        "rating": 4.5,
        "total_rating": 38,
        "description": "4K OLED evo display with Brightness Booster, Pixel Dimming, infinite contrast and perfect colours and viewing angles; 139 cm/55 inch screen size (measured diagonally); external dimensions (excluding stand): 122.2 x 70.3 x 4.51 cm; VESA standard: 300 x 200 mm, includes base. Smart TV: webOS 23 (LG ThinQ AI and AI Concierge) with Amazon Alexa, Hands Free Voice Control, Always Ready Function, Intelligent Voice Recognition, Apple AirPlay 2 and HomeKit; Home Dashboard, includes LG Magic remote control with NFC and 2 x AA batteries. Processor: α9 Gen6 4K AI processor with AI Picture Pro, AI Brightness Control, AI Acoustic Tuning, AI Picture Wizard, AI Concierge, AI Genre Selection and AI Sound Pro (Virtual 9.1.2 Up-mix); Gaming Features: NVIDIA G-SYNC and AMD FreeSync compatible, HGiG support, Game Optimiser (VRR/ALLM/QMS). Let off some steam with the Xbox Series S – Gilded Hunter Bundle, which includes nine in-game items and virtual currency for Fortnite, Rocket League and Fall Guys. Xbox Series S lets you experience next-generation speed and performance at an affordable price. Gilded Hunter Pack for Fortnite: Become the feared, teeth-baring and ruthless hunter with the Hunter Saber outfit, lead the weapon of legends upgraded with the Saber's Fang Pickaxe for modern combat, show your style with The Hunt Begins Wrap and spend 1,000 V-Bucks on your favourite Fortnite items."
    },
    {
        "title": "LG OLED65G39LA TV 165 cm (65 Inches) + Xbox Series S with Free Content",
        "url": "https://amzn.eu/d/a1Qp9H8",
        "image":"https://m.media-amazon.com/images/I/714pypqE8zL._AC_SL1500_.jpg",
        "price": 2738.99,
        "rating": 4.5,
        "total_rating": 10,
        "description": "4K OLED evo display with Brightness Booster Max, Light Control Architecture, pixel dimming, infinite contrast and perfect colours and viewing angles; 165 cm (65 inch) screen diagonal, external dimensions (without stand): 144.1 x 82.1 x 2.43 cm, VESA standard: 300 x 300 mm; includes zero-gap wall mount. Smart TV: webOS 23 (LG ThinQ AI & AI Concierge) with Amazon Alexa, Hands Free Voice Control, Always Ready Function, Intelligent Voice Recognition, Apple AirPlay 2 & HomeKit; Home Dashboard, Includes LG Magic Remote Control and 2x AA Batteries. Processor: α9 Gen6 4K AI Processor with AI Picture Pro, AI Brightness Control, AI Acoustic Tuning, AI Picture Wizard, AI Concierge, AI Genre Selection & AI Sound Pro (Virtual 9.1.2 Up-mix); Gaming Features: NVIDIA G-SYNC & AMD FreeSync Compatible, HGiG Support, Game Optimizer (VRR / ALLM / ALLM / MS). The Xbox Series S -Gilded Hunter Bundle, which includes nine in-game items and virtual currency for Fortnite, Rocket League and Fall Guys, you can really let off steam. Xbox Series S lets you experience next-generation speed and performance at an affordable price. Gilded Hunter Pack for Fortnite: Become the feared, teething and ruthless hunter with the Hunter Saber outfit, lead the weapon of legends upgraded with the Saber's Fang Pickaxe for modern combat, show your style with The Hunt Begins Wrap and give 1,000 V-Bucks for your favourite items in Fortnite from."
    },
    {
        "title": "Samsung QLED 4K Q60A TV 43 Inch (GQ43Q60AAUXZG), Quantum HDR, Quantum Processor Lite 4K, 100% Colour Volume",
        "url": "https://amzn.eu/d/b3NokOd",
        "image":"https://m.media-amazon.com/images/I/7133Lkaj9WS._AC_SL1500_.jpg",
        "price": 495.24,
        "rating": 4.5,
        "total_rating": 2087,
        "description": "Quantum HDR: Enjoy pictures with high contrast range. Quantum processor 4K Lite: Experience impressive power. OTS Lite: Experience sound that can follow movements. Quantum Dot technology: 100% colour volume in all brightness ranges. Contrast enhancer: Great depth and high colour contrasts."
    },
    {
        "title": "METZ Blue Roku TV, 4K UHD Smart TV, 43 Inches, 109 cm, TV with Triple Tuner, TV with WiFi, LAN, HDMI, USB, HDTV",
        "url": "https://amzn.eu/d/bstgywp",
        "image":"https://m.media-amazon.com/images/I/61pcHc70AvL._AC_SL1500_.jpg",
        "price": 279.34,
        "rating": 4.2,
        "total_rating": 236,
        "description": "Content and apps may vary depending on country. Roku services may not be available outside of Germany. 4K TV: Ultra HD TV with direct LED display (3840 x 2160 pixels) and HDR10. Triple tuner DVB-C/S2/T2 for all types of reception - satellite, cable and antenna. Perfect sound backdrop: 2 built-in speakers with Dolby Digital Plus, Dolby Digital and DTS Studio Sound. Free Roku app: control your TV, use voice search, audio via headphones and more. iOS and Android. Cross-channel search: search for titles, actors, genre and more and find out where to stream for free or at the lowest prices. Roku TV supports all popular voice assistants: Apple AirPlay, Apple Home, Alexa, Google Home. Apple TV+: New subscribers will receive 3 months free Apple TV+ upon registration until 29/05/2023."
    },
    {
        "title": "Xoro HTL 2477 60 cm (23.6 Inch) SmartTV HD TV with Integrated HD Triple Tuner (DVB-S2/T2/C), HbbTV",
        "url": "https://amzn.eu/d/6wrk8IP",
        "image":"https://m.media-amazon.com/images/I/81grdbmE91S._AC_SL1500_.jpg",
        "price": 175.11,
        "rating": 4.0,
        "total_rating": 34,
        "description": "The XORO HTL 2477 is equipped with a triple tuner for the reception of digital satellite, cable and antenna television. It offers extensive configuration options and powerful search functions. High resolution DLED HDTV panel for low consumption and excellent image quality. Supports CI+ modules (e.g. the CI+ module for receiving HD+ or Freenet TV). Thanks to the 12 V power connection, the device is also suitable for camping and caravans. With the built-in media player, you can play audio, video and image files from USB storage devices. Popular streaming portals are pre-installed, as well as a web browser on board. More apps can be downloaded and installed via the app portal. Thanks to the HbbTV support, you can use Internet content from TV stations (e.g. media librares)."
    },
    {
        "title": "Samsung QLED 4K Q60C 75 Inch TV + 2 x Xbox Wireless Controller Robot White + 9 Months Game Pass Ultimate",
        "url": "https://amzn.eu/d/ho22rLU",
        "image":"https://m.media-amazon.com/images/I/71kiJojq-JL._AC_SL1500_.jpg",
        "price":1682.09 ,
        "rating": 4.4,
        "total_rating": 1249,
        "description": "Thanks to Quantum Dot technology, up to 100% colour volume for rich colours in different brightness ranges. Enjoy high contrast range and film-ready images on the Samsung TV with Quantum HDR. Experience the modernized design of the Xbox Wireless Controller in Robot White, which provides more comfort when playing with its moulded surfaces and refined geometry. Stay on target course thanks to the textured grip surface and hybrid D pad. With your active subscription to Xbox Game Pass Ultimate, you can play games on Xbox One, Xbox Series X, and Windows 10 PC. Includes subscription to console games with Xbox Game Pass, subscription to PC games with Xbox Game Pass, EA Play and Xbox Live Gold."
    },
    {
        "title": "MEDION X15040 (MD 30606) 125.7 cm (50 Inch) QLED TV (UHD Smart TV, 4K Ultra HD, Dolby Vision HDR, Dolby Atmos, HDMI 2.1, Netflix, Prime Video, MEMC, Micro Dimming, PVR)",
        "url": "https://amzn.eu/d/fO1n5me",
        "image":"https://m.media-amazon.com/images/I/81v012u23bL._AC_SL1500_.jpg",
        "price": 429.99,
        "rating": 4.2,
        "total_rating": 1069,
        "description": "Elegant QLED Smart TV with HDR10, Dolby Vision, Dolby Atmos, DTS HD, DTS Virtual X, Micro Dimming, MEMC, CI+, WLAN, Bluetooth, PVR ready, media player, HbbTV, Netflix, Amazon Prime Video and other smart TV services. Just like in cinema: Dolby Vision will make your movies and series shine in brilliant colours and contrasts full of vibrancy. More brilliant than ever: High Dynamic Range (HDR10) allows lifelike contrast and colour. More details, more sharpness: Experience four times more detail with Ultra HD 4K resolution (3840 x 2160) than previous Full HD TVs. Box contents: Smart-TV X15040 MD30606, stand including screws, remote control including batteries (AAA), instruction manual (English language not guaranteed)."
    },
    {
        "title": "Samsung QLED 4K Q60C 75 Inch TV (GQ75Q60CAUXZG, German Model), Quantum Dot Technology, Quantum HDR, AirSlim Design, Smart TV ",
        "url": "https://amzn.eu/d/iJIGYNm",
        "image":"https://m.media-amazon.com/images/I/81a3fWRvUDL._AC_SL1500_.jpg",
        "price": 1339,
        "rating": 4.4,
        "total_rating": 1244,
        "description": "Thanks to Quantum Dot technology, up to 100% colour volume for rich colours in different brightness ranges. Enjoy high contrast range and film-ready images on the Samsung TV with Quantum HDR. AirSlim design fascinates with its filigree shape design, which allows the TV almost to merge with the wall. Samsung Smart Hub & Gaming Hub combine all your favourite smart TV and gaming apps in one place. Object Tracking Sound Lite creates a virtual sound that can follow different movements. "
    }
]

# Loop through the television data and add each television dictionary to the list
for television in television_data:
    televisions.append(television)
# Create an empty list to store solar panel dictionaries
solar_panels = []

solar_data = [
    {
        "title": "Solar Panel 100 Watt Mono 36 V Solar Panel Solar Cell 1130 x 505 x 30 93098 Photovoltaic",
        "url": "https://www.amazon.de/-/en/Solar-Panel-Watt-93098-Photovoltaic/dp/B086QNKV6X/ref=sr_1_8?crid=30Z3PLZ522RVH&keywords=solar+panels&qid=1697742972&s=industrial&sprefix=solar+panels%2Cindustrial%2C292&sr=1-8",
        "image":"https://m.media-amazon.com/images/I/61rI-XI+O5L._SY445_.jpg",
        "price": 88.95,
        "rating": 4.9,
        "total_rating": 20,
        "description": "Suitable for island systems. With modern 5-busbar technology and high-quality mono solar cells. TÜV-Saar tested quality modules, A-grade MONO, 100 W, 36 V. Proven quality directly from solartronics Germany. Ideal for 12V-24V systems on land or in mobile solar systems."
    }, 
    {
        "title": "ECO-WORTHY 120 W Solar Panel 12 V Kit, Solar Module Kit with Highly Efficient Monocrystalline Solar Panel and 30 A PWM Charge Controller",
        "url": "https://amzn.eu/d/f64xJWq",
        "image":"https://m.media-amazon.com/images/I/81dzyzPT6jL._AC_SX466_.jpg",
        "price": 81.59,
        "rating": 5,
        "total_rating": 3,
        "description": "Wide Application]: Daily power 480 Wh/day at 4 hours full of sunshine. Perfect for RVs, Caravans, Marines, Motorhomes, Electric Scooters, Golf Carts, Electric Wheels, Trolling Motors, Tool Trailers, Emergency Power Supply for Cabin Shed etc. Excellent Performance]: ECO-WORTHY solar panels use monocrystalline high-performance solar cells, which can provide up to 21.5% higher efficiency for sufficient lighting conditions. Corrosion-resistant aluminum alloy frame, so the panel can be used for decades and can withstand strong wind(2400Pa) and snow load (5400Pa) with long service life. The IP65 rated junction box provides complete protection. The back of the pre-drilled and plug and play cables allows for quick installation, the kit can be connected in series (24V) or parallel (12V) if needed. What you get: 120W mono solar panel + 1 set Z mounting brackets + 30A solar controller + 1 pair 16.4 feet 10A WG solar cable + 1 pair 2 in 1 connector + 1 pair 4.92 foot tray cable. 1 year with 24/7 technical support, if you have any problems or questions about the product, please feel free to contact us via Amazon or call the ECO-WORHTY hotline to get a solution. "
    },
    {
        "title": "ECO-WORTHY 120W 12V Monocrystalline Solar Panel",
        "url": "https://amzn.eu/d/3ZT3jNf",
        "image":"https://m.media-amazon.com/images/I/71NZYHtGt4L._SX466_.jpg",
        "price": 65.99,
        "rating": 4.5,
        "total_rating": 26,
        "description": "Wide range of applications: produces 480WH/day at 4 hours of full sunlight. The panel is ideal for charging a variety of 12V DC batteries such as wet, gel, MF, EFB and AGM batteries. Suitable for various scenarios such as caravans, cars, boats, marine, motorhomes, jet skis, caravans, water pumps, sheds, gardens, etc. Durable design: the panel can withstand strong winds (2400 Pa) and snow loads (5400 Pa); the durable aluminium frame allows the panel to work effectively even in harsh weather and provide you with efficient energy. Equipped with a waterproof IP65 junction box, which provides complete waterproof protection. Easy installation: With pre-drilled holes, the installation is easy to use and can be mounted on the roof or on the floor with the adjustable solar panel tilt brackets. They are directly compatible with ECO-WORTHY's floor brackets, Z brackets, angle brackets, mast brackets and tilt brackets. High efficiency: the solar panel is made of high-performance monocrystalline solar cells, which have a 21% higher efficiency than polycrystalline cells in bright weather, convert more light energy and are virtually maintenance-free. An integrated bypass diode minimizes power loss in the shade. ECO WORTHY offers you a 1-year warranty and 24/7 technical support, if you have any questions or concerns, please call ECO-WORTHY Hotline or contact us via Amazon. In case of transport damage, we can offer you a replacement or partial refund. Your satisfaction is guaranteed."
    },
    {
        "title": "Solar Panel, Lixada 30 W Portable Solar Panel Kit Set, IP65 Waterproof with Crocodile Clip, Solar Cell Solar Panel",
        "url": "https://amzn.eu/d/d5XPBWY",
        "image":"https://m.media-amazon.com/images/I/71Sd0KfImJL._AC_SX522_.jpg",
        "price": 35.46,
        "rating": 3.9,
        "total_rating": 8,
        "description": "Clean energy solar charging panel: solar energy, environmentally friendly, energy inexhaustible, cost-saving and user-friendly when you are driving, fishing, climbing, hiking and travelling anywhere. HIGH CRYSTALINE SILICONE & HIGH CONVERSION RATE:Monocrystalline solar panel with high conversion for safe and durable use, generates more energy and works better than traditional panels in strong sunlight, designed to produce maximum power to charge compatible devices in no time. Charging Port:Equipped with a crocodile clip, which is suitable as a power supply for various devices. IP65 Waterproof:Lxada solar panel rechargeable, no E-Xtra wires and IP65 waterproof ensures it is used in bad weather, portable and compact design, suitable for indoor and outdoor use.Extensive Use & Emergency Charging: Ideal suitable for outdoor life, camping, travel, picnic, home emergency and off-grid power outages, perfect and safe for various applications."
    },
    {
        "title": "Set of 4 for 2 Module Bracket for Solar Panel Stand for Solar Module Photovoltaic Mounting Set Adjustable Angle for Balcony, Flat Roof or Garden",
        "url": "https://amzn.eu/d/0WNw0Lc",
        "image":"https://m.media-amazon.com/images/I/51FMWIVAAZL.jpg",
        "price": 72.90,
        "rating": 3.1,
        "total_rating": 4,
        "description": "Safe and stable use: everything is screwed together. Adjustable mounting system for solar panels for solar systems, such as balcony power plants, ready-to-plug PV systems etc. Adjustable angle. Areas of use: balcony railings, lawn in the garden, flat roof, caravan, wall (facade), floor and much more. Easy to assemble with picture instructions. The stand is made of aluminium alloy with light weight. A large load capacity and strong stability is ensured. For solar panels dimensions: 1723 x 1134 x 30 mm."
    },
    {
        "title": "Solar Panel Monocrystalline Solar Panel, 165 W, 18 V for 12 V Batteries, Photovoltaic, Solar Cell Solar System, PV Solar System for Balcony",
        "url": "https://amzn.eu/d/bNzkQ51",
        "image":"https://m.media-amazon.com/images/I/A1P27ZJwMtL._SL1500_.jpg",
        "price": 89.80,
        "rating": 4,
        "total_rating": 241,
        "description": "Durable and maintenance-free: Our monocrystalline photovoltaic modules achieve a very high efficiency and the service life is at least 20 to 30 years. The maintenance required is also very low, as there is hardly any wear on the solar panel. The solar panel is often used when space problems or statical challenges are present. Safe and innovative: Monocrystalline photovoltaic solar panel technology is considered one of the most advanced solar panel technologies. On average it requires much less roof area to obtain sustainable energy compared to other technologies. Equipped with an IP65 protection device, it therefore has a touch protection. Therefore, dust cannot penetrate and the electrics are protected against jet water from all directions. Weather-resistant, resistant to cold and heat: Even in the most difficult weather conditions, the Kesser solar module shows no signs of weakness. Regardless of frost conditions, up to -40 °C or heat waves at a temperature of up to +85 °C, the solar panel is guaranteed to provide you with efficient energy. Thanks to the robust and rust-proof aluminium frame, the solar panel is also weather-resistant. Sustainable and economical: Join the sustainable people and make your contribution to a better environment while benefiting economically by producing cheap electricity and saving money. Thanks to the existing mounting device, the installation is quick and easy. Own power source: Solar system electricity. You can do it yourself. With our solar panel for feeding the solar power obtained into your own home network, you can actively participate in the energy revolution and thus save energy costs in no time. The high-quality PV system from Kesser ensures the best possible solar yields even in weaker lighting conditions."
    },
    {
        "title": "20W 12V Monocrystalline IP65 Waterproof DIY Solar Panel with 10A Solar Charge Portable Solar Panel Charger",
        "url": "https://amzn.eu/d/05FLAkr",
        "image":"https://m.media-amazon.com/images/I/71wxDd8xFbL._AC_SL1500_.jpg",
        "price": 55.31,
        "rating": 0,
        "total_rating": 0,
        "description": "Waterproof The solar charger is made of waterproof PET fabric, which has good waterproofing, can withstand harsh weather conditions, and is resistant to severe cold and heat. Effectively increase waterproofing, wear resistance, elasticity, heat resistance, etc., very suitable for outdoor activities. Portable The solar charging panel is mini size and lightweight design, does not take up space, durable, easy to carry and good quality. Semi-flexible, can be bent properly for a wider range of applications. Suitable for outdoor travel, mobile phones and tablets computers, electronic USB interface. Professional manufacturing, exquisite workmanship, high efficiency, stable performance and high reliability. High Efficiency This solar charger uses high efficiency solar panels with a photoelectric conversion rate of ≥21% and has higher charging efficiency. The solar panel has a built-in monocrystalline silicon solar panel that can convert solar energy into electricity and can be used as a solar charger for a 5 volt battery. Car & Motorcycle/Motorhome Equipment/Electroinstal"
    },
    {
        "title": "Solar Panel Kit 50W Solar Panel 60A Solar Charge Controller Set with 2 USB Outputs",
        "url": "https://amzn.eu/d/1NhGMSk",
        "image":"https://m.media-amazon.com/images/I/71nUUYr96mL._AC_SL1500_.jpg",
        "price": 45.74,
        "rating": 0,
        "total_rating": 0,
        "description": "Durable material: the chain switch is made of excellent material, strong sealing, heat resistant and not easy to rust. Areas of application: the pull chain switch is compatible with most chandeliers, fans, lamps and wall lights with pull chain switch control. Compact design: the pull chain cord switch adopts an exquisite and compact design that can be well homemade and hidden. Rated voltage: ceiling fan switches are designed for two voltage, maximum 3A at 250V or maximum 6A at 125V. 3-speed setting: ceiling light pull chain switch uses 3-speed adjustment and supports 4 wires for easy and convenient operation."
    },
    {
        "title": "180 Watt 36 V Mono Solar Module 10 Bus Bars 210 mm Cell Format Solar Panel",
        "url": "https://amzn.eu/d/1JnJbia",
        "image":"https://m.media-amazon.com/images/I/71M4oaQYS7L._SL1500_.jpg",
        "price": 127.95,
        "rating": 0,
        "total_rating": 0,
        "description": "solartronics Solar panel made of monocrystalline solar cells in new format. TÜV-Saar tested quality module, A-grade MONO, 180 W, 36 V. The solartronics M180-1200x775-36V solar module is a universal module with new 10-busbar technology in 210 mm cell format and high-quality mono solar cells. Our 180 W solar panel is suitable for island systems in design and performance data. Box contents: 1 piece, solar panel 180 W monocrystalline 36 V. Weight: 9.77 kg, dimensions: 1200 mm x 775 mm x 35 mm."
    },
    {
        "title": "120W 12V Monocrystalline Solar Panel for Motorhome Garden Camper Boat and Roof of the House",
        "url": "https://amzn.eu/d/hDhmjj6",
        "image":"https://m.media-amazon.com/images/I/71NZYHtGt4L._SL1500_.jpg",
        "price": 65.99,
        "rating": 4.5,
        "total_rating": 26,
        "description": "Wide range of applications: produces 480WH/day at 4 hours of full sunlight. The panel is ideal for charging a variety of 12V DC batteries such as wet, gel, MF, EFB and AGM batteries. Suitable for various scenarios such as caravans, cars, boats, marine, motorhomes, jet skis, caravans, water pumps, sheds, gardens, etc. Durable design: the panel can withstand strong winds (2400 Pa) and snow loads (5400 Pa); the durable aluminium frame allows the panel to work effectively even in harsh weather and provide you with efficient energy. Equipped with a waterproof IP65 junction box, which provides complete waterproof protection. Easy installation: With pre-drilled holes, the installation is easy to use and can be mounted on the roof or on the floor with the adjustable solar panel tilt brackets. They are directly compatible with ECO-WORTHY's floor brackets, Z brackets, angle brackets, mast brackets and tilt brackets. High efficiency: the solar panel is made of high-performance monocrystalline solar cells, which have a 21% higher efficiency than polycrystalline cells in bright weather, convert more light energy and are virtually maintenance-free. An integrated bypass diode minimizes power loss in the shade. ECO WORTHY offers you a 1-year warranty and 24/7 technical support, if you have any questions or concerns, please call ECO-WORTHY Hotline or contact us via Amazon. In case of transport damage, we can offer you a replacement or partial refund. Your satisfaction is guaranteed."
    }
]
# Loop through the solar data and add each solar panel dictionary to the list
for solar in solar_data:
    solar_panels.append(solar)

# Create an empty list to store headphones dictionaries
headphones = []
headphones_data = [
    {
        "title": "Sony WH-1000XM5 Wireless Industry Leading",
        "url": "https://amzn.eu/d/2wAFEKJ",
        "image":"https://m.media-amazon.com/images/I/61vJtKbAssL._AC_SL1500_.jpg",
        "price": 462.53,
        "rating": 4.5,
        "total_rating": 6863,
        "description": "Industry-leading noise cancellation: two processors control 8 microphones for unparalleled noise cancellation. With the Auto NC Optimizer, noise cancellation is automatically optimized based on your wearing conditions and environment. Beautiful sound, perfect with the new built-in V1 processor. Crystal clear talk with 4 beamforming microphones, precise voice recording and advanced audio signal processing. Up to 30 hours of battery life with quick charge (3 minutes charge for 3 hours playback). Ultra comfortable, lightweight design with soft leather. Multipoint connection allows you to quickly switch between devices. Carry your headphones effortlessly in the revised case. Description of age range: adult. Target gender: unisex."
    },
    {
        "title": "Sony WI-C310 Wireless In-Ear Headphones, 15 Hours Battery Life, Voice Assistant, Magnetic Earplugs, Behind-the-neck Design, Built-in Headset Function, Headset with Microphone",
        "url": "https://amzn.eu/d/dGrVP7Z",
        "image":"",
        "price": 34.95,
        "rating": 4.2,
        "total_rating":4425,
        "description": "Quick access to your favourite songs by voice and no more missed messages thanks to the built-in Google/Siri Assistant. Built-in headset function for hands-free calls. Up to 15 hours of battery life depending on the mode selected. Innovative design: neck band is lightweight and comfortable to wear. Wireless audio transmission with Bluetooth technology. Make calls with built-in microphone."
    },
    {
        "title": "Sony WH-CH520 Compact Easy to Carry Wireless Bluetooth On-Ear Headphones with Microphone (Black) Bundle with Protective Hard Case for Headphones (Pack of 2)",
        "url": "https://amzn.eu/d/gI8O8IQ",
        "image":"https://m.media-amazon.com/images/I/61BVXmG-KUL._AC_SL1500_.jpg",
        "price": 81.85,
        "rating": 4.6,
        "total_rating": 24,
        "description": "Box contents: Sony WH-CH520 compact, easy to carry wireless Bluetooth on-ear headphones with microphone (black) and hard case for headphones. LIGHTWEIGHT: Designed with comfort in mind, the WH-CH520 headphones are lightweight and feature soft ear pads, extra head cushions and silent joints so you can enjoy your favorite music and podcasts all day long. Easy hands-free calling: Thanks to the built-in microphone, you can make the conversation freely with the hands-free function. You don't even have to take your phone out of your pocket. MULTIPOINT CONNECTION For total convenience, this Bluetooth headphone can pair with two Bluetooth devices at the same time. Easily switch from a video or song on your laptop to a call on your phone, so you never miss a call. Quick pair: easily find your missing headphones by sound or check their last known location in the Google app 'My Device' on your smartphone."
    },
    {
        "title": "Sony MDR-Z1R High-Resolution Audio Kopfhörer (70mm High Definition-Treibereinheiten, Membran aus Flüssigkristallpolymerfolie,lautlose Gelenkstellen,Silber beschichtetes OFC Kabel) ,Schwarz",
        "url": "https://amzn.eu/d/3OwkbjU",
        "image":"https://m.media-amazon.com/images/I/616M7zrOi1L._AC_SL1250_.jpg",
        "price": 1818.71,
        "rating": 4.5,
        "total_rating": 108,
        "description": "Listen to the difference with massive 70 mm HD drivers, enjoy full-tone sound up to 120 kHz frequency response, listen to music at the highest level with Hi-Res audio compatibility. Keep the sound stable with a resonance-free all-metal housing, smooth sound at all frequencies with a Fibonacci patterned grill, ergonomic ear pad design. Beta Titan Headband, Genuine Leather Headband, Separate Ground Cable, Silver Plated OFC."
    },
    {
        "title": "Sony INZONE H3, MDR-G300 Wired Gaming Headset, Over-Ear Headphones with 360 Spatial Sound, Flip to Mute Microphone, App Support & PC Compatible (White)",
        "url": "https://amzn.eu/d/e66s18k",
        "image":"https://m.media-amazon.com/images/I/61R3vFaPZAL._AC_SL1500_.jpg",
        "price": 114.89,
        "rating": 4.3,
        "total_rating": 315,
        "description": "Personalised 360 spatial sound for gaming ensures precise rival detection. Game for hours of comfort with soft headband and smooth ear pads. Discord certified, clear communication via a flexible boom microphone with mute function. Ergonomically designed controls for effortless operation. Personalise your experience with the INZONE Hub software."
    },
    {
        "title": "Anker Soundcore Life Q30 Bluetooth Wireless Headphones With Active Noise Isolation, Hi-Res Sound, 40-Hour Battery, Fast Charging, For Home Office",
        "url": "https://amzn.eu/d/20T1zKX",
        "image":"https://m.media-amazon.com/images/I/61+WYAjltpL._AC_SL1500_.jpg",
        "price": 78,
        "rating": 4.5,
        "total_rating": 57063,
        "description": "Hi-res audio: Balanced middles, crystal clear trebles with 40 mm audio drivers for deep, intense hi-res sound profile. Even frequencies of up to 40 kHz are covered. Active noise cancellation: Effectively reduces up to 95% of all external noise such as cars and planes; ideal for music when travelling or in noisy environments. Individual modes: “Transport” for aircraft noise, “Outdoor” for road traffic and wind, and “Indoor” for office sounds and background conversations - the perfect solution for any situation. Non-stop music: Enjoy 40 hours of wireless playback time in ANC mode or even 60 hours of play time in standard mode! And if you’re in a hurry, your headphones can be charged for 4 hours of music within 5 minutes!. Comfort first: The velvety soft memory foam ear pads of the Life Q30 headphones, integrated in soft leather, give you flexible comfort while working or listening to music."
    },
    {
        "title": "Sennheiser Momentum 4 Wireless Headphones with Bluetooth White & BT T100 Bluetooth Audio Transmitter for Hi-Fi or Home Entertainment Black",
        "url": "https://amzn.eu/d/37s02ny",
        "image":"https://m.media-amazon.com/images/I/41x07fNPypL._AC_SL1001_.jpg",
        "price": 346,
        "rating": 4.8,
        "total_rating":20 ,
        "description": "Maximum audio resolution in characteristic Sennheiser sound: Enjoy first-class music quality all day long - the audiophile 42mm converter system and aptX Adaptive make it possible. Sound personalisation via the Sennheiser Smart Control app: sound adjustment via integrated equalizer, presets and sound modes for your individual preferences - for a unique sound experience. Undisturbed music enjoyment: Thanks to the adaptive noise cancellation, you can immerse yourself in the music - with the adjustable transparency mode, you can continue to hear ambient noise.  Exceptional comfort and long battery life: Lightweight, foldable design with padded headband and ear cushions for lasting comfort - Up to 60 hours of playtime with fast charge."
    },
    {
        "title": "Denon PerL Pro Premium True Wireless Headphones, Personalized Sound Profile with Masimo Adaptive Acoustic Technology, Noise Cancellation, Water Resistance and Built-in Microphones",
        "url": "https://amzn.eu/d/2SjKQKG",
        "image":"https://m.media-amazon.com/images/I/61YA1iQrUIL._AC_SL1500_.jpg",
        "price": 349,
        "rating": 4.1,
        "total_rating": 99,
        "description": "Masimo Adaptive Acoustic Technology (AAT) - Normal listening varies from person to person and can affect your listening experience. Masimo AAT automatically measures your listening sensation and creates a perfectly tailored profile. Qualcomm aptX Lossless - Delivers lossless and uncompressed CD quality sound via Bluetooth. No interruptions - Battery life per charge is up to eight hours. In addition, you can charge your in-ear headphones three times via the case.Freely configurable – with the Denon Headphones app, you can create your personal profile and customise your in-ear headphones."
    },
    {
        "title": "OnePlus Buds Z2 True Wireless Earbud Headphones, Touch Control with Charging Case, Active Noise Cancellation, IP55 Waterproof Stereo Headphones for Home, Sports, Pearl White",
        "url": "https://amzn.eu/d/8ZRoDDm",
        "image":"https://m.media-amazon.com/images/I/51fsFIagOoL._AC_SL1500_.jpg",
        "price": 108.64,
        "rating": 4.3,
        "total_rating": 338,
        "description": "Acoustically tuned for bigger, bolder beats with razor-sharp highs, with Dolby Atmos support, it's time to take your party anywhere. With a monster battery life up to 38 hours, make your party all day and night - and all day again. With Dash Charge, a 10-minute charge powers your music for 5 hours. Sync with your Android smartphone once you open the charging case - it's so fast. AI-powered noise reduction algorithms, noise-reducing microphones and an elegant design combine crystal clear calls. All-weather protection class IP55 for water and sweat resistance, the OnePlus Buds Z2 are perfect for outdoor and the gym. International products have separate terms, are sold from abroad and may differ from local products, including fit, age ratings, and language of product, labeling or instructions."
    },
    {
        "title": "beyerdynamic DT 240 PRO, Over-Ear Studio Headphones in Black Closed design, wired and plug-in cable.",
        "url": "https://amzn.eu/d/4WlFj04",
        "image":"https://m.media-amazon.com/images/I/71QWxO4mfzL._AC_SL1500_.jpg",
        "price": 99.59,
        "rating": 4.4,
        "total_rating": 1803,
        "description": "Professional studio headphones for monitoring and recording in compact over-ear design. Powerful drivers for distortion-free sound in the studio and on portable devices. Professional sound tuning for pure and precise reproduction. Outstanding noise isolation. Ergonomic headband and soft ear pads for hours of wearing comfort."
    },
]
# Loop through the headphones data and add each headphones dictionary to the list
for headphone in headphones_data:
    headphones.append(headphone)

# Create an empty list to store cuddly blanket dictionaries
cuddly_blanket = []

blanket_data = [
    {
        "title": "Bedsure Sherpa Double-Sided Blankets, Cuddly Blankets, Extra-Thick and Warm Sofa Blanket, Couch Blanket Made of Sherpa, Super-Fluffy Fleece Blanket as a Sofa Throw or Living Room Blanket",
        "url": "https://amzn.eu/d/jg7Kk5P",
        "image":"https://m.media-amazon.com/images/I/81I98hrxLvL._AC_SL1500_.jpg",
        "price": 27.99,
        "rating": 4.7,
        "total_rating": 32742,
        "description": "Material: this microfibre blanket is made from high-quality lambskin and flannel fleece. The sheepskin and fleece fabric bound with decorative knitted fabric make the blanket pleasantly cuddly, easy to clean and extremely durable. Sizes and colours: available in sizes 130 x 150 cm, 150 x 200 cm, 220 x 240 cm and 9 trendy colours: grey, charcoal grey, blue, red, purple and so on. In a particularly light-weight, fluffy, soft quality. The blanket with double-sided design will impress even the most discerning cuddle fans - whether old or young. You will love being pampered by its pleasant quality after a long day. Easy-care: machine wash in cold water on a low spin cycle, tumble dry on a low heat. Avoid direct heat. Thanks to the special processing technology, the fleece blanket will not shrink."
    },
    {
        "title": "Ratel Cuddly Blanket",
        "url": "https://amzn.eu/d/gWTa7JU",
        "image":"https://m.media-amazon.com/images/I/81ZuHLJMzoL._AC_SL1473_.jpg",
        "price": 19.99,
        "rating": 4.6,
        "total_rating": 11200,
        "description": "High-density microfibre: Made of 100% high-quality polyester fibre, soft and smooth to the touch with better resistance to fading and stains. Unlike cotton fibres, the microfibre blanket is not easy to deform and retains its shape after repeated washing. It is also anti-allergenic and more hygienic because synthetic fibres do not provide a breeding ground for mites. Perfect process: At 300 g/m², the thickened, double-sided, high-density velvet flannel blanket goes through multiple carding processes to increase blanket heat and prevent shedding. This results in a softer and more comfortable touch. Additionally, it has strong, clean seams for better strength and a better structural appearance. Resists well to washing. Multiple uses: blanket with a nice degree of softness that can be folded into a portable cylindrical shape that takes up very little space. It can be used as both a flat sheets and a sofa cover and is suitable for any season. Whether indoors or outdoors, you can use portable blankets to enjoy lasting warmth. It can be used for bedrooms, sofas, cars, camping, picnics and outdoor concerts. Easy care: the Ratel blanket can be machine washed at 40°C and is also suitable for tumble drying (at low temperatures). After washing and drying, the blanket quickly returns to its dry and fluffy state and can be used for a long time without becoming deformed. It even dries quickly in the cold of winter."
    },
    {
        "title": "Komfortec Sherpa Cuddly Blanket 150 x 200 cm Blanket, Bedspread, Fluffy Fleece Blanket, Sofa Blanket, Anthracite",
        "url": "https://amzn.eu/d/2ptmGL4",
        "image":"https://m.media-amazon.com/images/I/71xhfzM1b3L._AC_SL1500_.jpg",
        "price": 21.90,
        "rating": 5,
        "total_rating": 11,
        "description": "PREMIUM QUALITY REVERSIBLE SHERPA BLANKET: made from high quality 100% microfiber, Komfortec bedspread offer a soft and luxurious feel. Warmth, softness and style! The Komfortec Sherpa blanket is the perfect companion to snuggle up comfortably on chilly evenings and give you a heavenly feeling of comfort and relaxation. ULTIMATE WARMTH Komfortec winter blankets guarantee ultimate warmth and insulation for a restful night's sleep. WARMTH RATING The comforter has a 450gsm fill to keep you warm during the coldest months. Material: Flannel and Sherpa 450 g/m². Size options: 150 x 200 cm, 220 x 240 cm. Vacuum packed for environmentally friendly delivery. Environmentally friendly comfort: Oeko-Tex certified. No harmful substances in the materials. Snuggle up in comfort: sleep without the cold! Whether on the couch or in bed, this bedspread will quickly become a must have in your home. Take the cosiness and atmosphere of your living room to a new level with Komfortec first-class selection of decorative cushions and blankets. Washing and care: machine washable. Thanks to the easy-care material, the microfibre duvet dries exceptionally quickly. Choose a gentle cycle with temperatures up to 40 degrees Celsius, and you're done. Tumble dry gently, do not iron. Vacuum packed for protection. Please note that after opening the vacuum packaging, it may take up to 45 minutes for the product to regain its normal shape."
    },
    {
        "title": "MIULEE Cuddly Blanket, Fluffy Blanket, Fleece Blanket, Warm Sherpa Sofa Throw Blanket, Fluffy Throw, Microfibre Bedspread for Bed, Sofa, Bedroom, Office, 150 x 200 cm, White",
        "url": "https://amzn.eu/d/fBaC9ql",
        "image":"https://m.media-amazon.com/images/I/5183Ys09gKL._AC_SL1500_.jpg",
        "price": 29.74,
        "rating": 4.9,
        "total_rating": 37,
        "description": "UNIQUE DESIGN MIULEE high quality Sherpa blanket adopts double sided design, one side is 230GSM warm sherpa and the other side is 240GSM soft flannel fleece, which can provide you with different soft feelings. DECORATION The sherpa blanket comes in a variety of colors to meet your individual needs. With different colours to choose from, you will easily find the matching blanket to match your decor. Package: includes one piece 150 x 200 cm blanket. The fluffy soft flannel blanket with fleece top offers you different feelings of softness. MULTIPURPOSE - Snuggle up in the soft flannel fleece blanket from MIULEE while reading or sipping a cup of coffee on the sofa indoors or outdoors - Take a nap with the soft blanket instead of the heavy quilt when traveling, at a picnic or in the cool cinema. Easy to clean: the blanket is easy to wash. Machine washable in cold water. And tumble dry on low. You can use fabric softener to keep the blanket soft all the time."
    },
    {
        "title": "Snuggle Sac Cuddly Blanket, Fluffy Fleece Blanket, Blanket for Sofa, Bed, Couch, Warm and Soft Blanket with Striped Pattern, Blue, 200 x 225 cm",
        "url": "https://amzn.eu/d/9pZ3wnR",
        "image":"https://m.media-amazon.com/images/I/71t13gxqQtL._AC_SL1500_.jpg",
        "price": 29.99,
        "rating": 4.8,
        "total_rating": 92,
        "description": "High quality: this blanket is made of 100% polyester and has been brushed. The throw has achieved a balance of warmth and weight, and high-quality microfibers ensure that you feel softer warmer and do not sweat so quickly under the duvet cover. The throw blanket is suitable for all skin types, including children. IMPROVED DURABILITY: This Snuggle Sac flannel fleece blanket is strong and durable and features strong edges. Even after cleaning, the throw blanket does not fade, does not shed and is durable. VERSATILE We designed a special striped flannel blanket that serves as a bright home decoration. This lightweight blanket is ideal for bed, sofa or rocking chair at home. This soft blanket is a great living comfort for your family and pets!. GIFTABLE: this super soft and comfortable blanket is available in 3 colors and 4 sizes and comes with a beautiful gift box. It is perfect for your family and friends as a Christmas gift or as a housewarming gift for your fellow human beings. Easy care: the flannel fleece blanket can be machine washed between 30°C and 60°C and dried at low speed after washing to keep the blanket soft. Do not use bleach or cloth as chemicals may affect the softness of the blanket."
    },
    {
        "title": "Sherpa Double-Sided Blanket Fluffy Fabric Extra Soft Fleece Sherpa Bed Throw Fluffy and Improved Sleep Mink 150 x 200 cm",
        "url": "https://amzn.eu/d/bA1Mdp6",
        "image":"https://m.media-amazon.com/images/I/61JjlOkjUPL._AC_SL1024_.jpg",
        "price": 20.99,
        "rating": 4.4,
        "total_rating": 900,
        "description": "High quality polyester quality: Sherpa fleece blanket makes blankets made from 100% high-quality teddy fleece polyester fabric, which you will enjoy for a long time - this comfortable, cuddly, ultra-fluffy and warm Sherpa blanket is more fading and stain-resistant than cotton blankets - unlike cotton that is slightly elastic and does not retain its shape, a polyester blanket does not lose its shape over time. CHT. Cuddly soft luxury throw: Sherpa brings fluffiness to a new level with a refined finish. Snuggle up in and feel the warmth of a delicate hug for relaxation of body and mind. Heavyweight Luxury Sherpa Throw Blanket with Custom Double Stitched Edges Ideal for all weather conditions. ULTRA SOFT DOUBLE SIDED - Snuggle up in the pure softness of this Sherpa throw. Perfect as a bedspread for a bedroom or guest room, or simply as a throw for your couch. This luxurious blanket made from high quality teddy fleece not only looks like real fur, but also feels like real fur. It fits wonderfully with any existing decor. Treat yourself to this luxury every evening! Versatile use: Sitting on the couch or in bed or lying down with cuddly and warm Sherpa fleece blankets, perfect for indoor and outdoor use, provides pleasant warmth in cool weather, especially when camping and picnics."
    },
    {
        "title": "Aisbo Sofa Blanket, Cuddly Blanket, Grey, Extra Warm, Thick Sherpa Blanket, Huge Blanket, 230 x 270 cm, Soft, Fluffy, Sofa Throw, Couch Blanket",
        "url": "https://amzn.eu/d/gyM75cf",
        "image":"https://m.media-amazon.com/images/I/81u2Kf4eRwL._AC_SL1500_.jpg",
        "price": 44.99,
        "rating": 4.5,
        "total_rating": 1072,
        "description": "One side of the sofa blanket is made of delicate 220 g/m² flannel, which is particularly cuddly and skin-friendly, while the other side is made of fluffy 260 g/m² Sherpa, which keeps you nice and warm. The great combination allows you to enjoy the pleasant comfort from both sides. Thanks to the super soft properties of the materials, the fluffy fleece blanket is wrinkle-free and is perfect for cold autumn and winter time. In addition, the sofa blanket is manufactured to high quality standards with proper workmanship, making it durable and ensuring will retain its shape and colour for a long time. The simple and timeless design of the sofa blanket gives any room style and elegance and thanks to the different colour variations, you will definitely find a suitable blanket that matches your decor. Available in 4 sizes, everyone fits underneath, whether it’s children, individuals or couples, even with fully extended legs. Thanks to the reversible function, the grey blanket is versatile, and can be used either as a cuddly blanket for cosy TV evenings on the sofa, for reading hours in the study, or as a bedspread and sofa throw for daily protection. The Sherpa blanket will be a cosy everyday companion for you. The 230 x 270 cm blanket is machine washable on a cold cycle and can also be tumble dried on a low setting, so it is very easy to clean for everyday use, which means it is also a great gift idea for family and friends. "
    },
    {
        "title": "Beautissu Aurelia Microfibre Blanket 220 x 240 cm Coral Fleece Blanket Fluffy Bedspread",
        "url": "https://amzn.eu/d/bafK6vQ",
        "image":"https://m.media-amazon.com/images/I/71tvIkT5G2L._AC_SL1500_.jpg",
        "price": 23.99,
        "rating": 4.5,
        "total_rating": 4866,
        "description": "Microfibre coral fleece blanket. The Beautissu microfibre blanket with cashmere touch offers the highest quality and comfort and is ideal for warming, as a decoration or as a gift. Large cuddly surface. The very soft XXL blanket from Beautissu has a cuddly surface of 150 x 200 cm. The coral fleece polyester keeps the blanket particularly warm. Easy care: The cosy day blanket is made from 100% coral fleece and can be washed at 30°C. Thanks to the easy-care material, the microfibre blanket dries extremely quickly. Individually usable: Whether for your couch, sofa, double bed or single bed, with this high-quality and visually tasteful throw you not only provide an inviting environment, but also warm up on cold days. Oeko-Tex seal. This bedspread has the Oeko-Tex seal 'Textiles Vertrauen' (Confidence in Textiles). Oeko-Tex Standard 100 test number: 13.HHK.33921 Hohenstein HTTI."
    },
    {
        "title": "Zollner 024 Cuddly Blanket 150 x 200 cm or 220 x 240 cm Grey / White Fur Look, 150/200",
        "url": "https://amzn.eu/d/bVpHJzC",
        "image":"https://m.media-amazon.com/images/I/81SpTEZBqmL._AC_SL1500_.jpg",
        "price": 39.99,
        "rating": 4.7,
        "total_rating": 3941,
        "description": "One side of this blanket is made from white deep pile faux fur; the other made of beautifully smooth soft fleece. The fluffy reversible blanket made from 100% polyester is easy to clean, washable up to 30°C and has a pleasant weight of approx. 160 g / m². There are different comfort sizes, size approx. 150 x 200 cm or approx. 220 x 240 cm, perfect for snuggling up alone or together. This reversible blanket with grey fleece is very elegant and is a real eye-catcher in your living room. The good quality and the great inconspicuous inner hem make the blanket a special gem."
    },
    {
        "title": "Blumtal Fluffy, Cuddly Sherpa Blanket - High-Quality, Super Soft Fleece Blanket as Sofa Throw, Bedspread or Living Room Blanket",
        "url": "https://amzn.eu/d/fr5ri41",
        "image":"https://m.media-amazon.com/images/I/71OiWd27uHL._AC_SL1500_.jpg",
        "price": 22.99,
        "rating": 4.7,
        "total_rating": 5653,
        "description": "Soft and warm: the Blumtal fleece blanket is cuddly soft, beautiful and suitable for any season. The fleece side gives you a soft and cool feeling in summer and the fluffy Sherpa back keeps you warm in winter. Versatile: ideal for TV or reading evenings on the sofa. The Sherpa blanket can be quickly packed up and is therefore always the perfect companion, whether it's a picnic in the park, sports event or open air concert. High-quality material: the top is made from 100% microfibre fleece, the cuddly underside is made from 100% microfibre sherpa. The fleece blanket hardly loses colour even in direct sunlight. Highest quality requirements: tested for harmful substances according to standard 100 by Oeko-Tex (certificate number: 20.0.23116). Easy care: the fluffy blanket can be washed on a gentle cycle at 30 °C without losing its shape. Thanks to the easy-care material, the microfibre blanket dries extremely quickly."
    }
]
# Loop through the blanket data and add each blanket dictionary to the list
for blanket in blanket_data:
    cuddly_blanket.append(blanket)