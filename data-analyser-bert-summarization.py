# Download the summarizer
from summarizer import Summarizer
from summarizer.sbert import SBertSummarizer

# Load the summarizer
model = SBertSummarizer('paraphrase-MiniLM-L6-v2')

# Set the number of sentences to summarize
num_sentences = 5

# Set the body text
body = '''Spread over more than 253.38 acre, of which the waterbody comprises 180.60 acre, Madiwala lake in BTM layout was rejuvenated in 2018 with the addition of a biodiversity park. But a year later, the state government handed over the custody of the lake to the civic agency, Bruhat Bengaluru Mahanagara Palike (BBMP), claiming the decision would help in better upkeep of the waterbody. Environmental activists, however, said that the results have been quite the opposite since the change of guard. The lake was earlier with the Karnataka Forest Department.

Notably, the office of the Range Forest Officer is inside the lake area. Pointing at the poor maintenance of the lake, the officials from the forest department said that lavatories meant for the visitors are not functional and the fuses from the meter board at the amphitheatre area of the lake were taken away since the January electricity bill of Rs 16,000 was not paid.

A forest department official said, “The two lavatories that were constructed a few years ago are yet to be open to the public. The reason is that water connection has still not been provided to the lavatories. The trees are not maintained properly and only two staffers have been deployed by the BBMP for the upkeep of such a huge lake. We wanted to put up two information boards on birds frequenting the park of the lake but the BBMP denied us permission.”

“We want the lake to be given back to us so that the ecology of the lake is maintained well. It has been learnt from reliable sources that the custody of the lake will be given back to us later this year. The nursery and the butterfly park are in a shambles today. We used to generate Rs 25,000 on weekends and Rs 8,000 on weekdays from sale of tickets. But the BBMP has stopped boating services and it has withdrawn the entry fee,” he added.

In the recent tree census carried out by the civic agency, over 2,000 trees were counted at the lake. Officials said that more trees are yet to be counted.Lake activist Naveen S, who has planted hundreds of trees near the lake with the help of the forest department, accused the BBMP of neglecting the waterbody.

“During heavy monsoon, the untreated sewage enters the lake from the storm water drains (SWD). The BBMP has not addressed this issue. Most important, buildings have been built near the SWD and the lake, encroaching the buffer zone. Near the periphery of the lake, several bamboo trees were removed and when we requested the authorities to plant native species at vacant patches, the permission was denied,” he said.

Referring to the severe waterlogging that the BTM Layout faced last year during the monsoon, Naveen said: “The interconnectivity between Hulimavu lake and Madiwala lake has been adversely affected owing to the encroachment. We have found it difficult to even highlight the issues to the BBMP as their officers are unresponsive.”

The forest department had allotted a separate parking lot near the lake for the visitors. But after the transfer of the custody of the lake, the visitors now park their vehicles on the footpath and the road.

According to the Karnataka State Pollution Control Board (KSPCB), the water quality index of the lake is unsatisfactory and qualifies under Class D (propagation of wildlife and fisheries).

An engineer from the Bangalore Water Supply and Sewerage Board (BWSSB) informed that a sewage treatment plant (STP) with a 10 mld capacity is being constructed. “We will finish the work within 15 days and the STP will be operational. The work was delayed owing to reasons known only to the higher authorities,” he said.'''

# Summarize the text
result = model(body, num_sentences=num_sentences)

# Print the summary
print(result)