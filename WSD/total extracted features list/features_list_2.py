# بايگرم ، ترايگرم و پلاس يا ماينس فيچرها بايد قبل از حذف ستاپ-وردها از متن مورد سنجش قرارگيرند


########################### "فيچرهاي استخراج شده از پيکره متني با تارگت-ورد "کرم

krm_bagofwords_features5=['تبدیل','فاضلاب','زباله','مواد','ماده','معدن','تارتر','پوست',
                          'لجن‌زی','لجن','دریا','خاکی','خاک','دراز','پیله','ابریشم',
                          'پرورش','اشتغال','شغل','لقاءالله','الله','فضل','اولیاء','اولیا','ضیافت',
                          'الهی','پیامبر','پیام','اسلام','دین','اخلاق','منش',
                          'عدل','رفتار','روش','جعبه','پرورش‌دهندگان','انگل',
                          'روده','احشام','توت','برگ','آسیا','شرق',
                          'دفع','مبارزه','باغ','احمدیان','احمد','سعید',
                          'امین','علی','رضا','الجهاد','عبدالسلام','فرج',
                          'زهدی','رهبر','خالد','اسلامبولی','دشمن','انتقام',
                          'فرما','نما','خانه','مخلوط','فزا','افزا','فزود','افزود','شیر',
                          'جوش‌شیرین','حمله','سگ','سنگ','باد','درخت',
                          'گو','دوست','خونخوار','طب','خون‌گیری','خون','پرکار',
                          'محمدرضا','خلیل','خسرو','نوزاد','شاپرک',
                          'گرده','ذرت','آقا','زیردست','گروه','دریادل',
                          'بوشهر','رتینوئیک','درمان','‌لول','نگین',
                          'پادشاه','گدا','کشت','توصیف','عنصر','عناصر',
                          'فولاد','آستنیت','منگنز','نیکل','هدایت',
                          'الکتریکی','فلز','واسطه','اتمی','سخت',
                          'براق','خاکستر','نقره']

krm_bagofwords_features10=['کود','باریک','نوغان','حضرت','ابی‌الحسن‌الرضا',
                           'خداوند','مسلمان','درخت','کشاورز',
                           'ابراهیم','اله','آوانس','داریوش','مهدی','شهباز',
                           'ترور','جهاد','عشوه','آرد','زنجبیل',
                           'برکه','محمود','دوانی','جان',
                           'خوان','مقام','افتخار','تندیس','جشنواره',
                           'جوش','جوانی','تقویت','اسیر','رشت','پایدار',
                           'حرارت','انبساط','تناوب','جلا']

krm_bagofwords_features10more=['پدر','پسر','پارسا','پرهیزگار','ضیافت',
                               'بارگاه','بزرگوار','امام','جعفر','صادق',
                               'بشریت','سعادت','تکامل','نباتات','اسامی','اسم',
                               'دعوت‌شدگان','مسلحانه','مقاومت','کلاژن',
                               'پیگمانتاسیون‌','FDA','ظرفیت']

krm_calloc_i_plus1_features=['تارتر','پوست','لجن‌زی','لجن','ابریشم','کدو','زهدی','نما']

krm_calloc_i_minus1_features=['پیله','آقای','آقا','پرورش']

krm_bigrams=['فرود آ','خالد اسلامبولی']
krm_trigrams=['پیله کرم ابریشم','پرورش کرم ابریشم','توصیف این کرم']



########################### "فيچرهاي استخراج شده از پيکره متني با تارگت-ورد "شانه


shane_bagofwords_features5=['دست','لمس','سر','محاسن','عطر','سرمه‌دان','سرمه',
                            'گذاشت','روی','ارتفاع','زمین','برس','مو',
                            'ناراحت','پشت','آرواره','گردن','بازو',
                            'شکم','عرق','پذیرش','مسئولیت','پا',
                            'ردا','‌پوشان','دلیل','کتف','انگشت',
                            'مچ','آرنج','زانو','اجرا','مردم',
                            'راه','جاده','خاک','مسیر','سوال','سستی',
                            'بی‌مسئولیت','کار','اندازه‌گیری','اندازه','امتناع']

shane_bagofwords_features10=['پزشک','درد','احساس','ضربان','قلب',
                             'گیسو','سر','راه','ترافیک','آسفالت',
                             'بار','رکبی']

shane_bagofwords_features10more=['نظافت']

# فيچرهاي پلاس/ماينس مربوط بايگرم (يا ترايگرم) تارگت-ورد هستند
shane_calloc_i_plus1_features=['خالی','کن','کرد','خاکی']

shane_calloc_i_minus1_features=['روی']

#  بايگرم و ترايگرم ممکن است مربوط به هر یک از کلمات جمله باشند(نه فقط تارگت-ورد) و
#  با انديس تارگت-ورد کار ندارند بلکه فقط رخداد آن را در جمله چک مي کنند
shane_bigrams=['تنگی نفس','حمله قلبی']       
shane_trigrams=['شانه به شانه','از شانه تا']


########################### "فيچرهاي استخراج شده از پيکره متني با تارگت-ورد "شیر


shir_bagofwords_features5=['حوض','گوسفند','گريزان','شيميايي','بارداري',
                           'زن','باردار','لاكتوز','تربيت','عرب',
                           'ممزوج','رنده',',كره',
                           'كام','طعم','درازگوش','ليوان','خر','كاسه',
                           'گير','گاو','لبنيات','درند','روباه',
                           'ظرف','دهان','تكه','فيل',
                           'دنبال','شكار','دود','گرسنه','گله',
                           'هراس','بیا','امد','خفت','خواب','خورد','خور','گوشت',
                           'نان','اعتصاب','غريد','غر','جوجه','آگهي','بازرگاني',
                           'تبليغ','پوشك','بچه','مايعاتي','چاي','قهوه',
                           'توليد','كارخانه','مسموم','شكر','كاكائو','اضافه',
                           'بادام','ماهي','ميدان','جنگ','آب',
                           'فرآورده','حبوبات','اجاق','آجيل','كرم',
                           'آلوده','سبزي','جوشان','پيشگيري','نوزاد','مادر'
                           'طبيعي','بست','ده','صف','پا',
                           'كله','يال','دم','فرار','نر','سيرك',
                           'قفس','ليتر','سوييس','سرشير','قاشق',
                           'چرب','حلال','لبن','بستني','ماست','پنير',
                           'خامه','شاغل','داد','كودك','آهن',
                           'رشد','تغذيه','مكمل ','آسم','حساسيت',
                           'كلسيم','محصول','سبوس','پوك','عسل',
                           'مجلس','شمشير','فشار','مست','غران','سينه',
                           'سپر','پلنگ','مجسمه','دروازه','ويران','سرنگون',
                           'ايران','سرديس','زيرين','انبار','نقوش','نقش',
                           'خورشيد','سرباز','اسب','توپ','مينياتور','ماده','سنگ',
                           'هل','زنجبيل','رگولاتور','هواگير','هوا',
                           'يكطرفه','رانش','پمپ','بسته','فلكه','ارتفاع',
                           'ديگ','منبع','انبساط','وزنه','برق',
                           'مشعل','عيب','بخار','كنترل','سوخت',
                           'سروموتور','تابه','مجهز','شمعك','اتوماتيك','چدن','دستشويي',
                           'توالت','روشويي','ظرفشويي','شيلنگ','دوش','حمام',
                           'شستشو','باغبان','باغ','سرد','گرم','سرويس','تنظيم',
                           'بالانس','والو','سوزن','گاز',
                           'ترموستات','جريان','الكتريكي','تايمر','قطع','لولفوايد',
                           'ورود','واشر','وصل','لباسشويي','تخليه','ساندويچ',
                           'شتر','غرش','حمله','دوا','كوزه','پر']


shir_bagofwords_features10=['مغذي','پرورش','سيب','اسهال',
                            'بترس','شكار','كاميون','توزيع','كالري',
                            'سرطان','بستري','هم','زن','مركبات',
                            'توليد','پنير','فراپالايش','عدس','انفجار',
                            'غلات','آرد','زنجبيل','بيماري','وبا','ميكروب',
                            'چاقي','بقالي','ترس','وحشت','گريخت','گريز','كلسترول',
                            'مرخص','مصون','آلرژي','قلب','عروق','تراكم',
                            'استخوان','ويتامين','نگارگر','شكم','اشكانيان',
                            'معمار','هخامنشي','تعقيب','تاج','بالدار','ميل',
                            'پمپاژ','شبكه','آبرساني','دبي','زانو','فوت','جريان',
                            'لوپرش','دما','ترموستات','دمپر','راهه',
                            'شيلنگ','دستگاه','خروج','نصب',
                            'موتور','مواد','غذا','زايمان',
                            'ناقه','شيرخوار','طبيب']


shir_bagofwords_features10more=['انسان','حمايت','دشمن','ساختمان','ميكروب','بقالي',
                                'اسكوربوت','آهو','اتصالات','فولاد','سيفونه','سيال',
                                'لوله','مخزن','آبگيري','ماشين','مدار']


shir_calloc_i_plus1_features=['آب','مادر','گير','گرفت','گاو','خر','گفت',
                              'امد','خفت','آن','كم','اجاق','ده',
                              'نر','تازه','پرچربي','فشاري',
                              'ايران','فشار','هواگير','هوا','فلكه','اطمينان','برقي',
                              'برق','مغناطيسي','توالت','تكي','روشويي','ظرفشويي',
                              'تك','شيلنگي','شستشو','باغباني','سرد','گرم',
                              'متعادل','بالانس','سوزني','مخلوط','تنظيم','گاز',
                              'ترموستات','الكتريكي','داد','يكطرفه']


shir_calloc_i_minus1_features=['زبان','جوشاندن','مجسمه','ماده','رگولاتور',
                               'بسته','واشر','غرش']

shir_bigrams=['آب ميوه','تك واحدي','تخت جمشيد','سه راهه','كم چربي','بي چربي',
              'بدون چربي','صرفه جويي','جوش شيرين','تخم مرغ','مكمل آهن',
              'سرد و گرم','هم بزنيد','مواد غذايي','فشار شكن','خطوط توليد',
              'خط توليد']

shir_trigrams=['شيردهي','شيرزن','شيرخشك','شيرخوار','تابه گردان','شير كم چربي',
               'شير بي چربي','شير بدون چربي','شيرده']


