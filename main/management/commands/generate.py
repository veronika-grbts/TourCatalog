import requests
import random
from io import BytesIO
from django.core.files import File
from PIL import Image
from main.models import Tour
from faker import Faker
from decimal import Decimal

fake = Faker()
fake = Faker('uk_UA')


def fetch_image_from_url(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    image_io = BytesIO()
    image.save(image_io, 'PNG')
    image_io.seek(0)
    return File(image_io, name=f"tour_image_{random.randint(1, 1000)}.png")


def generate_fake_image_by_tour_type(tour_type):
    url = f'https://random.imagecdn.app/500/300?{tour_type}'
    return fetch_image_from_url(url)


def generate_tour_title(tour_type, country):

    title_templates = {
        'beach': f'Пляжний відпочинок на {country}',
        'excursion': f'Екскурсія по {country}',
        'ski': f'Гірськолижний відпочинок у {country}',
        'adventure': f'Пригодницький тур до {country}',
        'cruise': f'Круїз навколо {country}',
        'wellness': f'Оздоровчий тур до {country}',
        'safari': f'Сафари в {country}',
        'culinary': f'Кулінарний тур по {country}',
        'cultural': f'Культурний тур до {country}',
        'ecotourism': f'Екотуризм в {country}',
    }
    return title_templates.get(tour_type, f'Тур по {country}')


def generate_tour_description(tour_type, country):
        description_templates = {
            'beach': [
                f"Пориньте у теплі води та м'який пісок на {country}. Ідеальний тур для відпочинку на пляжі, з сонячними днями та можливістю насолодитися місцевою кухнею.",
                f"Ласкаво просимо на пляжі {country}! Золотий пісок, блакитна вода та тепле сонце — найкращий відпочинок на узбережжі.",
                f"Насолоджуйтеся безтурботними днями на пляжі {country}, де кожен знайде для себе відпочинок на будь-який смак.",
                f"Пляжний відпочинок у {country} — відпочиньте від метушні та насолоджуйтеся тишею і красивими краєвидами океану.",
                f"Виберіть {country} для ідеального пляжного відпочинку: чудові пляжі, лагідне море та безліч можливостей для активного відпочинку.",
                f"Насолоджуйтесь релаксацією на пляжах {country}, де ви можете спокійно відпочивати і засмагати під теплим сонцем.",
                f"Відпочинок на пляжах {country} — це ідеальний вибір для тих, хто шукає гармонію з природою та хоче відновити сили.",
                f"Мрійливі пляжі {country} чекають на вас! Забудьте про все та відпочивайте на узбережжі цієї прекрасної країни.",
                f"Якщо ви хочете провести ідеальну відпустку на пляжі, {country} — саме те місце, де ви зможете забути про все і насолоджуватись природою.",
                f"Пляжі {country} — це спокій та краса, які дозволять вам відпочити душею і тілом на сонячному узбережжі.",
                f"Відпочинок на пляжах {country} подарує вам незабутні моменти релаксації, де поєднуються приємне сонце та тепла вода.",
                f"Зануртесь у розслаблену атмосферу пляжів {country}, де кожен день — це можливість насолоджуватись чудовими пейзажами та природою.",
                f"Ідеальний пляжний відпочинок чекає вас у {country}. Затишок, природа і можливість покращити своє здоров'я — ось що вас чекає.",
                f"Вибір пляжного відпочинку у {country} — це можливість знайти внутрішній спокій серед краси місцевої природи та теплих вод.",
                f"Насолоджуйтесь чудовими пляжами {country} та чудовими умовами для активного відпочинку на воді."
            ],
            'excursion': [
                f"Відкрийте для себе історичні пам'ятки та культурну спадщину {country}. Наш тур по містах та селах подарує вам незабутні враження.",
                f"Подорожуйте по {country}, відвідуючи музеї, старовинні замки і насолоджуючись місцевою архітектурою.",
                f"Досліджуйте культурні та історичні багатства {country} у нашому екскурсійному турі, відвідуючи головні пам'ятки та місцеві традиції.",
                f"Пізнайте {country} через його історію та культуру: старовинні міста, прекрасні палаци та незабутні екскурсії.",
                f"Екскурсія по {country} — це можливість доторкнутися до історії та познайомитися з культурними традиціями країни.",
                f"Наші екскурсії по {country} допоможуть вам глибше зрозуміти багатство культури та історії цієї країни.",
                f"Зануртесь у минуле {country}, досліджуючи найвідоміші пам'ятки та архітектурні перлини.",
                f"Подорожуйте по {country}, відвідуючи старовинні замки, монастирі та прекрасні природні ландшафти.",
                f"Історія {country} розкривається перед вами під час наших екскурсій, що поєднують навчання і цікавість.",
                f"Відчуйте атмосферу {country}, відвідуючи найважливіші історичні та культурні пам'ятки цієї країни.",
                f"З нами ви відвідаєте стародавні міста, знамениті музеї і незвичайні культурні об'єкти {country}.",
                f"Екскурсії по {country} допоможуть вам дізнатися більше про його культуру, традиції та історичні особливості.",
                f"Подорожуйте по {country}, щоб дізнатися все про його чудову архітектуру, культуру та багату історію.",
                f"Відкрийте для себе {country}, відвідуючи місця, які оспівані в історії та літературі.",
                f"Незабутні екскурсії по {country} подарують вам нові враження та знайомство з культурними багатствами цієї чудової країни."
            ],
            'ski': [
                f"Гірськолижний відпочинок у {country} — ідеальне місце для любителів снігових схилів та захоплюючих зимових пейзажів.",
                f"Захоплюючий гірськолижний тур у {country}, де ви зможете насолодитися катанням на найкращих курортах та сніговими трасами.",
                f"Підкорюйте снігові вершини {country}! Наш тур дасть вам можливість насолодитися катанням на лижах та сноуборді.",
                f"Гірськолижний відпочинок у {country}: зимова казка на схилах гір, де кожен знайде трасу для себе.",
                f"Лижні курорти {country} — це ваш шанс поринути у світ зимових видів спорту та розкішних гірських пейзажів.",
                f"Гірськолижні курорти {country} чекають на вас! Справжня зимова казка, де на вас чекає безліч захоплюючих трас.",
                f"Незабутній гірськолижний відпочинок у {country}, де сніг і крижані вершини створюють ідеальні умови для активного відпочинку.",
                f"Якщо ви любите зимові види спорту, гірськолижний відпочинок у {country} — це саме те, що вам потрібно!",
                f"Відчуйте свободу на лижах і сноуборді у {country}, насолоджуючись чудовими гірськими ландшафтами та чистим повітрям.",
                f"Наш гірськолижний тур до {country} — це найкраще поєднання спорту, природи і гарного настрою.",
                f"Зимовий тур до {country} — це можливість відчути холод зимових гір і насолодитися неймовірними пейзажами."
            ],
            "adventure": [
                f"Приготуйтеся до неймовірних пригод у {country}, де вас чекають незабутні випробування та активний відпочинок на природі.",
                f"Відчуйте адреналін у {country} під час захоплюючих екстремальних активностей, що надовго залишать враження!",
                f"Ваша наступна велика пригода чекає на вас у {country}! Мандруйте по джунглях, підкорюйте гори та досліджуйте нові горизонти.",
                f"Екстремальний тур до {country} — це ідеальний вибір для тих, хто шукає нові враження та хоче відчути себе справжнім мандрівником.",
                f"Відкрийте для себе пригоди у {country}, де вас чекають незвідані території, активні види спорту та захоплюючі місця.",
                f"Готові до справжніх випробувань? Пригода в {country} дозволить вам відчути дух екстриму і нові враження від кожного кроку.",
                f"Відчуйте справжній екстрим у {country}, де кожен день — це нова пригода, що вимагає від вас мужності та рішучості.",
                f"Підкорюйте вершини і річки в {country}, відчуваючи дух пригод і природи, що надихає.",
                f"Захоплюючі активності на природі, неймовірні маршрути та екстремальні враження чекають вас у {country}.",
                f"Подорожуйте до {country} і пориньте в світ пригод, які змінять ваш погляд на життя!"
            ],
            "cruise": [
                f"Розкішний круїз по {country} подарує вам незабутні моменти релаксу та захоплюючих морських подорожей.",
                f"Запрошуємо на вишуканий круїз по {country}, де ви зможете насолодитися прекрасними пейзажами та комфортом на борту.",
                f"Досліджуйте {country} з моря, насолоджуючись затишком круїзу та захоплюючими видами на узбережжя.",
                f"Круїз по {country} — це ваш шанс відчути себе на розкішному лайнері, відкриваючи нові міста та мальовничі береги.",
                f"Морська подорож по {country} — це ідеальний вибір для тих, хто хоче відпочити на борту та досліджувати чудові узбережжя.",
                f"Справжній круїз по {country}: чудові пейзажі, комфорт та неймовірні морські пригоди чекають на вас.",
                f"Круїз по {country} — це можливість побачити найкращі узбережжя, острови та захоплюючі місця на борту розкішного корабля.",
                f"Відчуйте смак розкішного відпочинку на воді, вирушивши в круїз по {country}, де на вас чекає комфорт і емоції.",
                f"Наш круїз по {country} подарує вам незабутні емоції від морських подорожей та чарівних пейзажів узбережжя.",
                f"Розкішний круїз по {country} — це подорож, де поєднуються розваги на борту і неймовірні враження від морських краєвидів."
            ],
            "wellness": [
                f"Відпочиньте та відновіть сили в {country}, де вас чекають найкращі курорти та спа-послуги для вашого здоров'я.",
                f"Заслужений відпочинок у {country}: розслабляючі процедури, спа та курорти, які допоможуть вам відновити сили.",
                f"Оновіть свій дух і тіло в {country}, де вас чекають здорові процедури, релакс і відпочинок на природі.",
                f"Відчуйте повну гармонію і спокій на відпочинку в {country}, де кожен день — це крок до відновлення вашого балансу.",
                f"Здоров'я і спокій в {country}: розслабляючі курорти і спа, які допоможуть вам знайти внутрішню гармонію.",
                f"Пориньте у світ wellness відпочинку в {country}, де спа-процедури і здоровий спосіб життя повернуть вам енергію.",
                f"Оновіть своє тіло та душу на розкішних курортах {country}, де ви отримаєте комплексне оздоровлення та відпочинок.",
                f"Відпочинок для тіла і душі в {country}: спа, йога та природні процедури для вашого гармонійного відновлення.",
                f"Плануєте оздоровлення? Наш wellness-тур до {country} допоможе вам відновити сили і знайти баланс у житті.",
                f"Залиште стрес позаду та насолоджуйтесь відпочинком у {country}, де вас чекають розслаблюючі процедури і спа-послуги."
            ],
            'safari': [
                f"Неймовірне сафарі в {country}, де ви зможете побачити величезну кількість диких тварин у їх природному середовищі.",
                f"Захоплююче сафарі в {country} — це можливість побачити левів, слонів та інших великих тварин в дикій природі.",
                f"Приготуйтеся до захоплюючого сафарі в {country}, де вас чекають унікальні враження від спостереження за дикими тваринами.",
                f"Сафарі в {country} — це можливість потрапити в серце дикої природи та побачити тварин в їх природному середовищі.",
                f"Ваша пригода чекає на вас у {country}: вирушайте на сафарі та спостерігайте за тваринами, які залишаються в дикій природі.",
                f"Сафарі по {country} — це незабутня подорож серед безкраїх саван і джунглів, де живуть дивовижні тварини.",
                f"Пориньте в світ дикої природи на сафарі в {country}, де ви зможете побачити тварин, яких мало хто може зустріти в природному середовищі.",
                f"Вирушайте на незабутнє сафарі в {country}, де у вас буде можливість побачити унікальні види тварин і рослин.",
                f"Сафарі в {country}: незабутнє знайомство з тваринами, природою та культурними пам'ятками цієї чудової країни.",
                f"Чекаєте на захоплюючу пригоду? Сафарі в {country} — це шанс відчути справжній дух дикої природи."
            ],
            'culinary': [
                f"Відкрийте для себе смак {country} через кулінарні традиції: найкращі страви та рецепти, що захоплюють уяву.",
                f"Справжня кулінарна подорож по {country}: відвідайте найкращі ресторани, щоб насолодитися місцевими делікатесами.",
                f"Наш кулінарний тур по {country} подарує вам можливість скуштувати традиційні страви, приготовані за старовинними рецептами.",
                f"Подорожуйте по {country} і відкрийте для себе унікальні страви, які стануть справжнім святом для вашого смаку.",
                f"Зануртесь в культуру {country} через їжу: знайомтесь з місцевими кухарями та відкривайте нові смаки в кожній страві.",
                f"Кулінарний тур по {country}: від шеф-кухарів до вуличних торговців — відкрийте для себе гастрономічні чудеса цієї країни.",
                f"Відчуйте кулінарну магію {country}, де ви зможете навчитися готувати місцеві страви та дегустувати смачні національні делікатеси.",
                f"Кулінарна подорож по {country} — це можливість поринути в атмосферу місцевої кухні та насолодитися кожним кроком на гастрономічному маршруті.",
                f"Гастрономічний тур по {country}: відкривайте нові смаки, традиції та культурні особливості кухні цієї країни.",
                f"Досліджуйте кулінарні секрети {country}, смакуючи страви, що переносять вас у саме серце культури цієї чудової країни."
            ],
            'cultural': [
                f"Насолоджуйтесь культурною спадщиною {country} з нашим туром, який охоплює найкращі музеї, архітектурні пам'ятки та історичні місця.",
                f"Поглиблене знайомство з культурою {country} через відвідування місцевих музеїв, галерей і історичних пам'яток.",
                f"Історична та культурна подорож по {country}, де ви зможете дізнатися більше про традиції та спадщину цієї неймовірної країни.",
                f"Зануртесь у культуру {country}, відвідуючи важливі історичні місця, музеї та національні святині.",
                f"Культурний тур по {country}: відвідайте історичні об'єкти, храми та культові місця, щоб зрозуміти, що формує цей народ.",
                f"Наш культурний тур по {country} допоможе вам відчути душу цієї країни через її історію, мистецтво та архітектуру.",
                f"Відкрийте для себе багатство культури {country}: від стародавніх архітектурних шедеврів до сучасних культурних центрів.",
                f"Культурний тур по {country}: ідеальний вибір для тих, хто хоче пізнати історію та мистецтво цієї країни на глибшому рівні.",
                f"Ваша подорож до {country} — це шанс побачити культурні скарби країни, від її величних архітектурних споруд до традиційних ремесел.",
                f"Зануртесь у культуру {country}, відвідуючи місцеві фестивалі, концерти та інші культурні події, що знайомлять вас з її спадщиною."
            ],
            'ecotourism': [
                f"Відкрийте для себе екологічно чисті куточки {country} та досліджуйте природу, яку треба зберігати для майбутніх поколінь.",
                f"Екотуризм у {country}: пізнайте природні чудеса країни, підтримуючи ініціативи зі збереження навколишнього середовища.",
                f"Подорожуйте екологічно чистими маршрутами в {country}, де ви будете відпочивати, пізнаючи природу та культуру одночасно.",
                f"Збереження природи та відпочинок на свіжому повітрі в {country}: екотуризм — це можливість поєднати відпочинок і турботу про природу.",
                f"Досліджуйте природні заповідники та національні парки {country}, де кожен крок наближає вас до чудес природи.",
                f"Екотуризм у {country} — це можливість відчути гармонію з природою, відвідуючи нетуристичні маршрути та збережені природні місця.",
                f"Пориньте в екологічно чисту атмосферу {country}, відвідуючи екологічні курорти, національні парки та природні резервати.",
                f"Подорожуйте по {country}, дотримуючись принципів екотуризму: насолоджуйтеся природою, підтримуючи її збереження.",
                f"Екотуризм у {country} — це шанс відкрити для себе місця, які залишаються неторкнутими людським впливом, і допомогти зберегти їх.",
                f"Зануртесь у природу {country}, обираючи екологічні тури та подорожуючи без шкоди для навколишнього середовища."
            ]

        }

        return random.choice(description_templates.get(tour_type, []))


def create_fake_tour():
    tour_type = random.choice([
        'beach', 'excursion', 'ski', 'adventure', 'cruise',
        'wellness', 'safari', 'culinary', 'cultural', 'ecotourism'
    ])

    country = fake.country()
    title = generate_tour_title(tour_type, country)
    description = generate_tour_description(tour_type, country)
    duration = random.randint(1, 14)
    price = Decimal(random.uniform(2500, 100500)).quantize(Decimal('0.01'))  # случайная цена
    rating = round(random.uniform(0.0, 5.0), 1)
    image = None
    # 50% вероятность добавить изображение
    if random.choice([True, False]):
        image = generate_fake_image_by_tour_type(tour_type)

    tour = Tour(
        title=title,
        description=description,
        country=country,
        duration=duration,
        price=price,
        tour_type=tour_type,
        rating=rating,
        image=image
    )
    tour.save()


def generate_fake_tours(count=2):
    for _ in range(count):
        create_fake_tour()

generate_fake_tours(2)
