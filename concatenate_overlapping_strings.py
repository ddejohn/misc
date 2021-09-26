import itertools


def get_match(s1, s2, min_overlap=3):
    """
    'Slides' `s2` from the left over the end of `s1`,
    starting at `min_overlap`. Adds all common subtstrings
    that are found and returns the longest among them.
    """
    i = min_overlap
    matches = []
    while i < min(len(s1), len(s2)):
        if s1[-i:] != s2[:i]:
            i += 1
            continue
        matches.append(s1[-i:])
        i += 1
    return max(matches, key=len) if matches else None


def get_links_and_joiners(strings):
    """
    Links will be key:value pairs of words that have a common
    substring where the end of `s1` overlaps with the start of `s2`.
    """
    links = dict()
    joiners = set()
    for s1, s2 in itertools.permutations(strings, 2):
        match = get_match(s1, s2)
        if match:
            joiners.add(match)
            links[s1] = s2
    return links, joiners


def get_ordered_strings(strings, links):
    """
    A recursive closure which determines the length of each sequence
    starting at `node` and traversing the `links` dictionary.
    """
    def find_order(node):
        return 0 if node not in links else 1 + find_order(links[node])
    return sorted(strings, key=find_order, reverse=True)


def join_strings(strings, joiners):
    """
    Joins an ordered sequence of `strings`, removing the extraneous `joiner`
    between each pair of joins.
    """
    s = "".join(strings)
    for j in joiners:
        s = s.replace(j, "", 1)
    return s


strings = ["THREEFOUR",
           "ONESTRING",
           "STRINGTHREE",
           "FOURFIVE",
           "HOWDY",
           "PARTNER",
           "HELLO",
           "WORLD"]

links, joiners = get_links_and_joiners(strings)
ordered_strings = get_ordered_strings(strings, links)
join_strings(ordered_strings, joiners)

# OR only join strings which form a pair based on a common substring
matched_only = get_ordered_strings(set(links) | set(links.values()), links)
join_strings(matched_only, joiners)
