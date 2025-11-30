def invite_guests(guestlist):
    for each_guest in guestlist:
        print(f"Dear {each_guest}, you are cordially invited to dinner at my place this Saturday at 7 PM.")
    return

def not_coming(guestlist, absent_guest):
    guestlist.remove(absent_guest)
    return guestlist

def new_guest(guestlist, new_guest_name):
    guestlist.append(new_guest_name)
    return guestlist

guestlist = ['Scott', 'Nancy', 'Dan', 'Noel', 'Liz']

invite_guests(guestlist)
absent_guest = 'Dan'
print(f"\nUnfortunately, {absent_guest} can't make it to the dinner.\n")
guestlist = not_coming(guestlist, absent_guest)
new_guest_name = 'Mike'
guestlist = new_guest(guestlist, new_guest_name)
invite_guests(guestlist)   

print("\nGood news! I've found a bigger dinner table, so I'm inviting more guests.\n")
guestlist.insert(0, 'Laura')
guestlist.insert(3, 'Jim')
guestlist.append('Jane')

invite_guests(guestlist)
print("\nUnfortunately, the new dinner table won't arrive in time, and I can only invite two guests.\n")
while len(guestlist) > 2:
    removed_guest = guestlist.pop()
    print(f"Dear {removed_guest}, I'm sorry to inform you that I can no longer invite you to dinner.")
print()
invite_guests(guestlist)    

guestlist.clear()
print(f"\nFinal guest list: {guestlist}")
