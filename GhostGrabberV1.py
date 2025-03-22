import time
from colorama import init, Fore, Style

# Initialize colorama for Windows compatibility
init()

def display_info_box():
    # Rainbow colors for the title and box
    rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    
    # Rainbow title
    title = "║                                   FUCK THE ACE LETS WATCH IT FOR FREE!                             ║"
    rainbow_title = ""
    for i, char in enumerate(title):
        rainbow_title += rainbow_colors[i % len(rainbow_colors)] + char
    rainbow_title += Style.RESET_ALL

    # Box lines with rainbow colors
    lines = [
        "╔════════════════════════════════════════════════════════════════════════════════════════════════════╗",
        "║                                                                                                    ║",  # Top padding
        "║                                                                                                    ║",  # Extra padding
        rainbow_title.center(100),  # Centered rainbow title
        "║                                                                                                    ║",  # Spacing
        "║   Creator: YourAnonSp1r1t                                                                          ║",
        "║                                                                                                    ║",  # Spacing
        "║   Twitter: x.com/YourAnonSp1r1t                                                                    ║",
        "║                                                                                                    ║",  # Spacing
        "║   Version: 1.1                                                                                     ║",
        "║                                                                                                    ║",  # Extra padding
        "║                                                                                                    ║",  # Bottom padding
        "╚════════════════════════════════════════════════════════════════════════════════════════════════════╝"
    ]

    # Print each line with rainbow effect
    for line in lines:
        if line == rainbow_title.center(100):  # Skip re-coloring the title since it's already rainbow
            print(line)
        else:
            rainbow_line = ""
            for i, char in enumerate(line):
                rainbow_line += rainbow_colors[i % len(rainbow_colors)] + char
            rainbow_line += Style.RESET_ALL
            print(rainbow_line)
    print()  # Empty line after the box

def simulate_web_search():
    # Rainbow colors for searching text
    rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    
    # Initial search message with rainbow effect
    search_msg = "Searching web for piracy sites..."
    rainbow_search = ""
    for i, char in enumerate(search_msg):
        rainbow_search += rainbow_colors[i % len(rainbow_colors)] + char
    rainbow_search += Style.RESET_ALL
    print(rainbow_search)
    time.sleep(10)
    
    # Simulate searching different browsers with rainbow effect
    browsers = [
        "Searching Google...",
        "Searching Opera GX...",
        "Searching Bing...",
        "Searching DuckDuckGo...",
        "Searching Microsoft Edge..."
    ]
    delays = [17, 20, 15, 20, 25]
    
    for browser, delay in zip(browsers, delays):
        rainbow_browser = ""
        for i, char in enumerate(browser):
            rainbow_browser += rainbow_colors[i % len(rainbow_colors)] + char
        rainbow_browser += Style.RESET_ALL
        print(rainbow_browser)
        time.sleep(delay)
    
    # List of piracy sites
    piracy_sites = [
        "web.netmovies.to",
        "fmovies24.one",
        "dopebox.to",
        "alphatron.tv",
        "hianime.to",
        "sflix2.to",
        "fmoviesmax.com",
        "actvid.rs",
        "mapple.tv",
        "fmovies24.watch",
        "moviestowatch.tv",
        "123movies.sc",
        "ww.yesmovies.ag",
        "hdtodayz.to",
        "myflixer.pw",
        "moviesjoytv.to",
        "vipstream.tv",
        "pressplay.top",
        "movies2watch.is"
    ]
    
    # Display results with light blue header and green sites
    print(f"\n{Fore.CYAN}Piracy sites found:{Style.RESET_ALL}")  # Light blue for the header
    for site in piracy_sites:
        print(Fore.GREEN + site + Style.RESET_ALL)
    
    # Pause before exiting
    input(f"\n{Fore.CYAN}Press Enter to exit...{Style.RESET_ALL}")

# Run the program
if __name__ == "__main__":
    # Show the info box first
    display_info_box()
    # Wait for user to press Enter to start the simulation
    input(f"{Fore.CYAN}Press Enter To Start DeepWebSearch{Style.RESET_ALL}")
    # Start the simulation
    simulate_web_search()