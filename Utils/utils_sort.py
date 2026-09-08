
def bubble_sort(lst, key=lambda x: x, reverse=False):
    n = len(lst)
    sortat = False

    while not sortat:
        sortat = True
        for i in range(n - 1):
            if key(lst[i]) > key(lst[i + 1]):
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                sortat = False

    if reverse:
        lst.reverse()

    return lst

def shell_sort(lst, key=lambda x: x, reverse=False):
    n = len(lst)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = lst[i]
            j = i

            while j >= gap and key(lst[j - gap]) > key(temp):
                lst[j] = lst[j - gap]
                j -= gap

            lst[j] = temp

        gap //= 2

    if reverse:
        lst.reverse()

    return lst


def generic_sort(lst, *, key=lambda x: x, reverse=False, method="bubble"):
    copie = lst[:]   # NU modificăm lista originală

    if method == "bubble":
        return bubble_sort(copie, key=key, reverse=reverse)
    elif method == "shell":
        return shell_sort(copie, key=key, reverse=reverse)
    else:
        raise ValueError("Metodă de sortare necunoscută")

