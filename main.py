import logging
import preprocess
logging.basicConfig(level=logging.INFO)

train, valid, test, others = preprocess.get_data()

train = preprocess.merge_utterance(train)
valid = preprocess.merge_utterance(valid)
test = preprocess.merge_utterance(test)

preprocess.merge_plustag(train)
preprocess.merge_plustag(valid)
preprocess.merge_plustag(test)

preprocess.merge_act_tag(train, show_actmap=True)
preprocess.merge_act_tag(valid)
preprocess.merge_act_tag(test)
