def get_num_words(book_text):
       num_words=len(book_text.split())
       return num_words

def count_characters(book_text):
       count_dict={}
       for char in book_text:
              char=char.lower()
              if char not in count_dict:
                   count_dict[char]=0
              count_dict[char]+=1
       return count_dict

# Helper function for sorting
def sort_on(item):
              return item["num"]

#This is the actual sorting
def sorter(count_dict):
       sorted_character_counts=[]
       for char in count_dict:
              tempdict={"char": char , "num": count_dict[char]}
              sorted_character_counts.append(tempdict) 

       sorted_character_counts.sort(reverse=True, key=sort_on)
       return sorted_character_counts