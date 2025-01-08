#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Original list of guests
guests = ["Albert Einstein", "Marie Curie", "Leonardo da Vinci"]

# One guest can't make it
print("Unfortunately, Leonardo da Vinci can't make it to dinner.")

# Replace the guest who can't make it
guests[2] = "Nikola Tesla"

# Print new invitation messages
for guest in guests:
    print(f"Dear {guest}, you are cordially invited to dinner at my place. Please join us for an evening of great conversation!")

