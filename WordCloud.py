import wordcloud
from matplotlib import pyplot as plt

file_contents = "The morning of April 25, 2015, arrived with only a whisper of wind. Sailboats traced gentle circles " \
                "on Alabama’s Mobile Bay, preparing for a race south to the coast. On board the Kyla, a lightweight "  \
                "16-foot catamaran, Ron Gaston and Hana Blalack practiced trapezing. He tethered his hip harness to "  \
                "the boat, then leaned back over the water as the boat tilted and the hull under their feet went "     \
                "airborne. “Physics,” he said, grinning. They made an unusual crew. He was tall and lanky, "           \
                "50 years old, with thinning hair and decades of sailing experience. She was 15, tiny and pale and "   \
                "redheaded, and had never stepped on a sailboat. But Hana trusted Ron, who was like a father to her. " \
                "And Ron’s daughter, Sarah, was like a sister.The Dauphin Island Regatta first took place more than "  \
                "half a century ago and hasn’t changed much since. One day each spring, sailors gather in central "    \
                "Mobile Bay and sprint 18 nautical miles south to the island, near the mouth of the bay in the Gulf "  \
                "of Mexico. There were other boats like Ron’s, Hobie Cats that could be pulled by hand onto a beach. " \
                "There were also sleek, purpose-built race boats with oversized masts—the nautical equivalent of "     \
                "turbocharged engines—and great oceangoing vessels with plush cabins belowdecks. Their captains were " \
                "just as varied in skill and experience. A ripple of discontent moved through the crews as the boats " \
                "circled, waiting. The day before, the National Weather Service had issued a warning: “A few strong "  \
                "to severe storms possible on Saturday. Main Threat: Damaging wind. ”Now, at 7:44 a.m., as sailors "   \
                "began to gather on the bay for a 9:30 start, the yacht club’s website posted a message about the "    \
                "race in red script: "


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers",
                           "its","they", "them","their", "what", "which", "who", "whom", "this", "that", "am", "are",
                           "was", "were", "be","been", "being", "have", "has", "had", "do", "does", "did", "but", "at",
                           "by", "with", "from", "here", "when","where", "how", "all", "any", "both", "each", "few", "more",
                           "some", "such", "no", "nor", "too", "very","can", "will", "just", "in", "on", "for"]

    new_content = ""
    for index, i in enumerate(file_contents):
        if i not in punctuations:
            new_content += file_contents[index]
    print(new_content)
    words = new_content.split()

    print(words)

    word_dict = {}
    for word in words:
        word = word.lower()
        if word not in uninteresting_words:
            if word.isalpha():
                if word not in word_dict:
                    word_dict[word] = 1
                else:
                    word_dict[word] += 1
    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_dict)
    return cloud.to_array()
   

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation='nearest')
plt.axis('off')
plt.show()
