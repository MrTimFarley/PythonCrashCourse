favorite_languages = {
      'jen': ['python', 'ruby'],
      'sarah': ['c'],
      'edward': ['C++', 'java'],
      'phil': ['python', 'swift'],
      }

print("The following languages have been mentioned:")
all_languages = []
for languages in favorite_languages.values():
    all_languages.extend(languages)

for language in set(all_languages):
    print(language.title())

