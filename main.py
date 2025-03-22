import time
import requests
import random
import msvcrt  # For single key press detection on Windows
import os
import sys
from colorama import init, Fore, Style

# Initialize colorama for Windows compatibility
init()


def display_info_box(color_scheme):
    if color_scheme == 'R':  # Rainbow
        colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    elif color_scheme == 'B':  # Blue
        colors = [Fore.BLUE]
    elif color_scheme == 'G':  # Green
        colors = [Fore.GREEN]
    else:  # Default to Rainbow if invalid input
        colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

    title = "║                             FUCK THE A.C.E LETS WATCH IT FOR FREE!!!                               ║"
    colored_title = "".join(
        colors[i % len(colors)] + Style.BRIGHT + char for i, char in enumerate(title)) + Style.RESET_ALL

    creator = "║   Creator: YourAnonSp1r1t                                                                          ║"
    twitter = "║   Twitter: x.com/YourAnonSp1r1t                                                                    ║"
    version = "║   Version: 1.3                                                                                     ║"
    colored_creator = "".join(
        colors[i % len(colors)] + Style.BRIGHT + char for i, char in enumerate(creator)) + Style.RESET_ALL
    colored_twitter = "".join(
        colors[i % len(colors)] + Style.BRIGHT + char for i, char in enumerate(twitter)) + Style.RESET_ALL
    colored_version = "".join(
        colors[i % len(colors)] + Style.BRIGHT + char for i, char in enumerate(version)) + Style.RESET_ALL

    lines = [
        "╔════════════════════════════════════════════════════════════════════════════════════════════════════╗",
        "║                                                                                                    ║",
        "║                                                                                                    ║",
        colored_title.center(100),
        "║                                                                                                    ║",
        colored_creator,
        "║                                                                                                    ║",
        colored_twitter,
        "║                                                                                                    ║",
        colored_version,
        "║                                                                                                    ║",
        "║                                                                                                    ║",
        "╚════════════════════════════════════════════════════════════════════════════════════════════════════╝"
    ]

    for line in lines:
        if line in [colored_title.center(100), colored_creator, colored_twitter, colored_version]:
            print(line)
        else:
            colored_line = "".join(colors[i % len(colors)] + char for i, char in enumerate(line)) + Style.RESET_ALL
            print(colored_line)
    print()


def check_site_status(url):
    try:
        response = requests.get(f"https://{url}", timeout=10)
        return "[UP]" if response.status_code in [200, 202, 403] else "[DOWN]"
    except:
        return "[DOWN]"


def simulate_web_search(color_scheme, search_depth):
    if color_scheme == 'R':
        colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
        header_color = Fore.CYAN
        site_color = Fore.GREEN
        status_color = Fore.YELLOW
    elif color_scheme == 'B':
        colors = [Fore.BLUE]
        header_color = Fore.BLUE
        site_color = Fore.BLUE
        status_color = Fore.BLUE
    elif color_scheme == 'G':
        colors = [Fore.GREEN]
        header_color = Fore.GREEN
        site_color = Fore.GREEN
        status_color = Fore.GREEN
    else:
        colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
        header_color = Fore.CYAN
        site_color = Fore.GREEN
        status_color = Fore.YELLOW

    if search_depth == 'S':
        delay_factor = 0.5
    elif search_depth == 'M':
        delay_factor = 1.0
    else:  # 'D' or default
        delay_factor = 1.5

    search_msg = f"Searching web for piracy sites... (Depth: {search_depth})"
    print("".join(colors[i % len(colors)] + char for i, char in enumerate(search_msg)) + Style.RESET_ALL)
    # time.sleep(10 * delay_factor)

    hacker_messages = [
        "Bypassing corporate firewalls...",
        "Cracking into the dark web...",
        "YourAnonSp1r1t says: Freedom is ours!",
        "Scrambling ISP trackers...",
        "Hunting for hidden streams...",
        "Punching through the matrix...",
        "Stealing from the streaming overlords!"
    ]

    browsers = ["Searching Google...", "Searching Opera GX...", "Searching Bing...", "Searching DuckDuckGo...",
                "Searching Microsoft Edge..."]
    delays = [10, 15, 10, 15, 20]
    for browser, delay in zip(browsers, delays):
        print("".join(colors[i % len(colors)] + char for i, char in enumerate(browser)) + Style.RESET_ALL)
        # time.sleep((delay * delay_factor) / 2)
        hack_msg = random.choice(hacker_messages)
        print(f"{Fore.MAGENTA}{hack_msg}{Style.RESET_ALL}")
        # time.sleep((delay * delay_factor) / 2)

    anime_sites = [
        "hianime.to", "animeheaven.me", "9animetv.to", "anilab.to", "aniwave.uk",
        "anime.nexus", "anitaku.io", "animekai.to", "gogoanime.org.vc", "animepahe.ru",
        "kaa.mx", "animez.org", "www.animegg.org", "kissanime.com.ru", "allmanga.to",
        "aniworld.to", "nyaa.land", "w1.123animes.ru", "www.wcostream.tv"
    ]

    movie_show_sites = [
        "web.netmovies.to", "fmovies24.one", "dopebox.to", "alphatron.tv", "sflix2.to", "fmoviesmax.com",
        "actvid.rs", "mapple.tv", "fmovies24.watch", "moviestowatch.tv", "123movies.sc", "ww.yesmovies.ag",
        "hdtodayz.to", "myflixer.pw", "moviesjoytv.to", "vipstream.tv", "pressplay.top", "movies2watch.is",
        "m.wcostream.tv", "www.wcostream.tv", "flixbaba.com", "watchonmovie.com/US", "watchstream.site",
        "www.youplex.site", "plexmovies.online", "sunnymovies.site", "ww1.goojara.to", "wmovies.xyz",
        "www.vidbinge.com", "www.cineby.app", "myflixerz.to", "hydrahd.ac", "www.popcornmovies.to",
        "www.lookmovie2.to", "onionplay.ch", "gomovies.sx", "primeflix.lol", "watch.ug/home",
        "theflixertv.to", "sflix.to", "projectfreetv.sx"
    ]

    if search_depth == 'S':  # Surface: ~25%
        anime_sites = anime_sites[:max(1, len(anime_sites) // 4)]
        movie_show_sites = movie_show_sites[:max(1, len(movie_show_sites) // 4)]
    elif search_depth == 'M':  # Medium: 50%
        anime_sites = anime_sites[:len(anime_sites) // 2]
        movie_show_sites = movie_show_sites[:len(movie_show_sites) // 2]
    # 'D' (Deep) shows full list, no slicing

    bogus_sources = ["[Tor Network]", "[Hacker Forum]", "[Google Cache]", "[Dark Pool]", "[Anon Leak]", "[Deep Scan]"]
    scan_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE]

    print(f"\n{header_color}Anime Sites Found:{Style.RESET_ALL}")
    for site in anime_sites:
        print(f"{Fore.CYAN}Discovering...{Style.RESET_ALL}", end="\r")
        # time.sleep(0.5)
        status = check_site_status(site)
        source = random.choice(bogus_sources)
        for i in range(4):
            print(f"{site_color}{site:<20} {scan_colors[i]}Scanning...{Style.RESET_ALL}", end="\r")
            # time.sleep(0.4)
        print(f"{site_color}{site:<20} {status_color}{status} {Fore.MAGENTA}{source}{Style.RESET_ALL}")

    print(f"\n{header_color}Movie & Shows Sites Found:{Style.RESET_ALL}")
    for site in movie_show_sites:
        print(f"{Fore.CYAN}Discovering...{Style.RESET_ALL}", end="\r")
        # time.sleep(0.5)
        status = check_site_status(site)
        source = random.choice(bogus_sources)
        for i in range(4):
            print(f"{site_color}{site:<20} {scan_colors[i]}Scanning...{Style.RESET_ALL}", end="\r")
            # time.sleep(0.4)
        print(f"{site_color}{site:<20} {status_color}{status} {Fore.MAGENTA}{source}{Style.RESET_ALL}")

    print(f"\n{Fore.RED}NOTE: The Ones That Say Down MAY NOT ACTUALLY BE DOWN, CHECK Them First{Style.RESET_ALL}")
    print(f"\n{header_color}Press Enter to exit or R to restart in new window...{Style.RESET_ALL}", end="", flush=True)

    # Wait for single key press
    while True:
        key = msvcrt.getch().decode('utf-8').upper()
        if key == '\r':  # Enter key
            return False  # Exit
        elif key == 'R':
            # Launch a new instance of the script in a new window
            script_path = os.path.abspath(__file__)  # Get the full path of this script
            os.startfile(script_path)  # Open it in a new terminal window
            sys.exit(0)  # Exit the current instance
        # Ignore other keys and keep waiting


if __name__ == "__main__":
    print(f"{Fore.CYAN}Choose a color scheme:{Style.RESET_ALL}")
    print(
        f"{Fore.RED}R{Style.RESET_ALL} for Rainbow, {Fore.BLUE}B{Style.RESET_ALL} for Blue, {Fore.GREEN}G{Style.RESET_ALL} for Green")
    color_scheme = input("Enter your choice (R/B/G): ").upper()

    display_info_box(color_scheme)

    print(f"{Fore.CYAN}How deep should we search?{Style.RESET_ALL}")
    print(
        f"{Fore.RED}S{Style.RESET_ALL} for Surface, {Fore.YELLOW}M{Style.RESET_ALL} for Medium, {Fore.GREEN}D{Style.RESET_ALL} for Deep")
    search_depth = input("Enter your choice (S/M/D): ").upper()

    if search_depth == 'S':
        input(f"{Fore.CYAN}Press Enter To Start SmallWebSearch{Style.RESET_ALL}")
    elif search_depth == 'M':
        input(f"{Fore.CYAN}Press Enter To Start MidwayWebSearch{Style.RESET_ALL}")
    else:  # 'D' or anything else
        input(f"{Fore.CYAN}Press Enter To Start DeepWebSearch{Style.RESET_ALL}")

    simulate_web_search(color_scheme, search_depth)
