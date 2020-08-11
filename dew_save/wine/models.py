from django.db import models
from django.core.validators import MaxLengthValidator
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.core.validators import FileExtensionValidator
from django.utils import timezone
from django.contrib.auth import get_user_model



# Create your models here.


class Wine(models.Model):

    sort_data = [
        ('red', 'red'),
        ('white', 'white'),
        ('sparkling', 'sparkling'),
    ]
    

    country_data = [
        ('France', 'France'),
        ('Italy','Italy'),
        ('Germany', 'Germany'),
        ('Spain', 'Spain'),
        ('Portugal', 'Portugal'),
        ('USA', 'USA'),
        ('Australia', 'Australia'),
        ('New Zealand', 'New Zealand'),
        ('Argentina', 'Argentina'),
        ('Chile', 'Chile'),
        ('South Africa', 'South Africa'),
        ('Japan', 'Japan'),
        ('etc.', 'etc.'),
    ]
    
    vintage_data = [
        ('1980', '1980'), ('1981', '1981'), ('1982', '1982'), ('1983', '1983'), ('1984', '1984'), ('1985', '1985'), 
        ('1986', '1986'), ('1987', '1987'), ('1988', '1988'), ('1989', '1989'), ('1990', '1990'), ('1991', '1991'), 
        ('1992', '1992'), ('1993', '1993'), ('1994', '1994'), ('1995', '1995'), ('1996', '1996'), ('1997', '1997'), 
        ('1998', '1998'), ('1999', '1999'), ('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'),
        ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'),
        ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'),
        ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), 
    ]

    grape_data = [
        ('Chardonnay', 'Chardonnay'),
        ('Sauvignon Blanc', 'Sauvignon Blanc'),
        ('Riesling', 'Riesling'),
        ('Gewürztraminer', 'Gewürztraminer'),
        ('Semillon', 'Semillon'),
        ('Viognier', 'Viognier'),
        ('Pino Blanc', 'Pino Blanc'),
        ('Muscadet', 'Muscadet'),
        ('Pino gris', 'Pino gris'),
        ('Cortese', 'Cortese'),
        ('Trebbiano', 'Trebbiano'),
        ('Garganega', 'Garganega'),
        ('Malvasia', 'Malvasia'),
        ('Chenin Blanc', 'Chenin Blanc'),
        ('Albariño', 'Albariño'),
        ('甲州', '甲州'),
        ('etc.', 'etc.'),
    ]

    eye_data = [
        ('green', 'green'),
        ('lemon yellow', 'lemon yellow'),
        ('yellow', 'yellow'),
        ('gold', 'gold'),
        ('amber', 'amber'),
    ]

    nose_data = [
        ('lemmon', 'レモン'), ('kime', 'ライム'), ('grapefruit', 'グレープフルーツ'), ('apple', 'リンゴ'), ('green apple', '青りんご'),
        ('pear', '洋ナシ'), ('peach', '桃'), ('apricot', 'アプリコット'), ('pineapple', 'パイナップル'), ('passion fruit', 'パッションフルーツ'),
        ('banana', 'バナナ'), ('mango', 'マンゴー'), ('lychee', 'ライチ'), ('muscat', 'マスカット'), ('water melon', 'メロン'),
        ('kinmokusei', 'キンモクセイ'), ('mint', 'ミント'), ('rose', 'バラ'), ('floral', 'お花のような'), ('herb', 'ハーブの'), ('perfume', '香水'),
        ('barrel incense', '樽香'), ('toast', 'トースト'), ('butter', 'バター'), ('vanila', 'バニラ'), ('sulfur', '硫黄'), ('honey', 'はちみつ'),
        ('cinnamon', 'シナモン'),('mineral', 'ミネラル'),
    ]

    mouth_data = [
        ('fresh', 'フレッシュ感のある'),
        ('dry', 'ドライな'),
        ('sour', '酸味が目立つ'),
        ('balance', 'バランスの良い'),
        ('sweat', '甘さのある'),
        ('fruity','フルーツ感のある'),
        ('elegant', 'エレガントな,綺麗な'),
        ('mineral','ミネラルのある'),
        ('rich', '芳醇な、豊かな'),
        ('thick', '厚みのある'),
        ('strong', '濃縮し力強い'),
        ('aging', '長期熟成型のような'),
    ]

    error_msg = [
        '50文字まででお願いします。',
        '10文字まででお願い致します。',
        '点数は5点までで採点お願い致します。',
        '点数は0点以上で採点お願い致します。',
        'ファイル形式はJPEG,PNG,GIFでお願い致します。'
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,default=1)
    date = models.DateTimeField(default=timezone.now)
    name = models.CharField(verbose_name='Name', max_length=100,validators=[MaxLengthValidator(50,error_msg[0])])
    sort = models.CharField(verbose_name='Sort',choices=sort_data,max_length=100)
    country = models.CharField(verbose_name='Country', choices=country_data,max_length=100)
    vintage = models.CharField(verbose_name='Vintage', choices=vintage_data,max_length=100,blank=True)
    grape = models.CharField(verbose_name='Grape', choices=grape_data,max_length=100,blank=True)
    eye = models.CharField(verbose_name='Eye', choices=eye_data,max_length=100,blank=True)
    nose = models.CharField(verbose_name='Nose', choices=nose_data,max_length=100,blank=True)
    mouth = models.CharField(verbose_name='Mouth', choices=mouth_data,max_length=100,blank=True)
    memo = models.CharField(verbose_name='Memo', max_length=30, blank=True)
    point = models.FloatField(verbose_name='Point',validators=[MaxValueValidator(5,error_msg[2]),MinValueValidator(0,error_msg[3])])
    pic = models.ImageField(upload_to='images/',blank=True,validators=[FileExtensionValidator(['JPG','PNG','GIF'],error_msg[4])])


    def __str__(self):
        return 'WineID:' + str(self.id) + ',' + str(self.sort) + ' wine'