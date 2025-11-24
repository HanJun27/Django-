# 在项目根目录创建 create_sample_data.py 文件
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music.settings')
django.setup()

from index.models import Label, Song, Dynamic

def create_sample_data():
    # 创建音乐分类
    pop_label, created = Label.objects.get_or_create(label_name='流行音乐')
    rock_label, created = Label.objects.get_or_create(label_name='摇滚音乐')
    classical_label, created = Label.objects.get_or_create(label_name='古典音乐')
    
    # 创建示例歌曲
    sample_songs = [
        {
            'song_name': '示例歌曲1',
            'song_singer': '示例歌手1',
            'song_time': '03:45',
            'song_album': '示例专辑1',
            'song_languages': '中文',
            'song_company': '示例唱片公司',
            'song_release': '2023-01-01',
            'song_img': 'default.jpg',
            'song_lyrics': '暂无歌词',
            'song_file': 'sample1.mp3',
            'label': pop_label
        },
        {
            'song_name': '示例歌曲2', 
            'song_singer': '示例歌手2',
            'song_time': '04:20',
            'song_album': '示例专辑2',
            'song_languages': '英文',
            'song_company': '示例唱片公司',
            'song_release': '2023-02-01',
            'song_img': 'default.jpg',
            'song_lyrics': '暂无歌词',
            'song_file': 'sample2.mp3',
            'label': rock_label
        },
        {
            'song_name': '示例歌曲3',
            'song_singer': '示例歌手3', 
            'song_time': '05:15',
            'song_album': '示例专辑3',
            'song_languages': '纯音乐',
            'song_company': '示例唱片公司',
            'song_release': '2023-03-01',
            'song_img': 'default.jpg',
            'song_lyrics': '暂无歌词',
            'song_file': 'sample3.mp3',
            'label': classical_label
        }
    ]
    
    for song_data in sample_songs:
        song, created = Song.objects.get_or_create(
            song_name=song_data['song_name'],
            defaults=song_data
        )
        if created:
            # 创建对应的动态数据
            Dynamic.objects.create(
                song=song,
                dynamic_plays=0,
                dynamic_search=0,
                dynamic_down=0
            )
            print(f"创建歌曲: {song.song_name}")
        else:
            print(f"歌曲已存在: {song.song_name}")

if __name__ == '__main__':
    create_sample_data()
    print("示例数据创建完成！")