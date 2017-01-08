from django.core.management.base import BaseCommand, CommandError
from mainapp.models import CactusGenus, CactusSubfamily, ViewCactus


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        subfamilys = [{'name': 'Цереусовые',
                            'description': 'Древовидные, кустящиеся или ветвящиеся растения с хорошо развитой кроной,'
                                           ' от 1,5 до 15 м высотой, до 50 см диаметром, с мощной корневой системой и '
                                           'высокими, прямыми, острыми ребрами. Радиальные колючки жесткие, крепкие, '
                                           'прямые до 3см длиной, центральные – шиловидные, 3-10 см длиной. '
                                           'Окрас колючек от серого и коричневого до красного и черного.',
                            'image': "ceriusov.jpg"},
                           {'name': 'Опунцивые',
                            'description': 'К опунциевым относятся прямостоячие и стелющиеся кустарники или'
                                           ' кустарнички, часто подушковидной формы. Стебли сочные,'
                                           ' шаровидные, дисковидные, овальные, состоящие из отдельных'
                                           ' члеников или цилиндрические. Листья сочные, шиловидные, '
                                           'мелкие, скороопадающие. Цветки колосовидные, крупные, '
                                           'с раздражимыми тычинками. Окраска цветков желтая, оранжевая, белая.'
                                           ' Семена в отличие от всех прочих кактусов плоские, с твердой оболочкой.',
                            'image': "opunchivie.jpg"},
                           {'name': 'Перескивые',
                            'description': 'К подсемейству относятся 3 рода. В культуре чаще встречаются два из них, '
                                           'внешний облик которых меньше всего соответствует привычному представлению о'
                                           ' кактусах.',
                            'image': "perescivie.jpg"}
                           ]
        cactusGenuses = [{'name': 'Astrophitum',
                        'description': 'Астрофитум (Astrophytum) – небольшой род растений семейства Кактусовые '
                                           '(Cactaceae), в котором уверенно можно выделить всего 5 видов, '
                                           'распространённых на юге США и севере Мексики. '
                                           'К настоящему времени многочисленные классификаторы так и не смогли сойтись'
                                           ' во мнении, сколько именно представителей у данного рода, так как даже'
                                           ' внутривидовые морфологические признаки растений сильно зависят от места'
                                           ' их произрастания.',
                        'subfamily': 'Цереусовые'},
                        {'name': 'Aztekium',
                        'description': 'Ацте́киум (лат. Aztekium) — род растений из семейства кактусовых, включающий '
                                       'в себя три небольших шаровидных вида.Открытый в 1929 году Ф. Риттером, в '
                                       'Районесе (штат Нуэво-Леон, Мексика), этот род был первоначально описан, как '
                                       'монотипный (с видом Aztekium ritteri).',
                         'subfamily': 'Цереусовые'},
                        {'name': 'Gymnocalycium',
                        'description': 'Гимнокалициум представляет собой шаровидное растение с длинными, чуть'
                                       ' изогнутыми колючками. Форму шара обычно имеет молодой кактус. По мере роста '
                                       'его ствол приобретает ребристую цилиндрическую форму. Самые маленькие его '
                                       'представители вырастают не более 3 см, самые крупные могут быть высотой до'
                                       ' полуметра.',
                         'subfamily': 'Цереусовые'}
                        ]
        ViewCactuss = [{
                'type': 'asterias',
                'genus':  'Astrophitum',
                'image': 'Astrophytum_asterias.jpg',
                'complexity_of_cultivation': 'Средний',
                'area': 'Мексика, Техас',
                'price': '50',
                'diametr': '20'},
            {
                'type': 'ritteri',
                'genus':  'Aztekium',
                'image': 'aztekium_ritteri.jpg',
                'complexity_of_cultivation': 'Сложный',
                'area': 'Мексика',
                'price': '180',
                'diametr': '8'
            },
            {
                'type': 'friedrichii',
                'genus':  'Gymnocalycium',
                'area': 'Парагвай',
                'image':'gymnocalycium_friedrichii',
                'complexity_of_cultivation': 'Простой',
                'price': '20',
                'diametr': '15'
            }]

        CactusSubfamily.objects.all().delete()
        for subfamily in subfamilys:
            cactusSubfamily = CactusSubfamily(**subfamily)
            cactusSubfamily.save()

        CactusGenus.objects.all().delete()
        for cactusGenus in cactusGenuses:
            gen_name = cactusGenus['subfamily']
            subfamily = CactusSubfamily.objects.get(name=gen_name)
            cactusGenus['subfamily'] = subfamily
            cactusGenus = CactusGenus(**cactusGenus)
            cactusGenus.save()

        ViewCactus.objects.all().delete()
        for cactus in ViewCactuss:
            gen_name = cactus['genus']
            genus = CactusGenus.objects.get(name=gen_name)
            cactus['genus'] = genus
            cactus = ViewCactus(**cactus)
            cactus.save()
