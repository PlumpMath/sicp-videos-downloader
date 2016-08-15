from pyquery import PyQuery as pq

ARCHIVE_URL = 'https://archive.org/details/mit_ocw_sicp&tab=collection'
BASE_DOWNLOAD_URL = 'https://archive.org/download/'

DIRECTORY_LISTING_KEYWORD = '/details/halmit'
VIDEO_KEYWORD = '.mpg'


def write_video_urls(video_urls, dst):
    with open(dst, 'w') as o:
        o.write('\n'.join(video_urls))


def _get_video_url(dl_url, video_a_tags):
    for a_tag in video_a_tags:
        href = a_tag.get('href')
        if href and (VIDEO_KEYWORD in href):
            url = dl_url + '/' + href
            return url


def _get_directory_listing_url(video_a_tags):
    for a_tag in video_a_tags:
        href = a_tag.get('href')
        if href and (DIRECTORY_LISTING_KEYWORD in href):
            yield BASE_DOWNLOAD_URL + href.replace('/details/', '')


def get_video_urls(dl_a_tags):
    video_urls = []
    for dl_url in _get_directory_listing_url(dl_a_tags):
        v_d = pq(dl_url)
        video_a_tags = v_d('a')
        video_url = _get_video_url(dl_url, video_a_tags)
        video_urls.append(video_url)
    return video_urls


def main():
    dl_d = pq(ARCHIVE_URL)
    dl_a_tags = dl_d('a')
    print('ALL DIRECTORY LIST URLS PARSED!')

    video_urls = get_video_urls(dl_a_tags)
    print('ALL VIDEO URLS PARSED!')

    return video_urls

if __name__ in ['__main__', '__console__']:
    video_urls = main()
    write_video_urls(video_urls, dst='sicp-video-urls.txt')
