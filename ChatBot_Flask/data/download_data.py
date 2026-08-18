import os
import json
import logging
from datasets import load_dataset

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
log = logging.getLogger(__name__)

fname = 'academic_persona_chat.json'
max_len = 3  # Limit the number of sessions


def get_data():
    try:
        if os.path.exists(fname):
            log.info('If already exists, skip')
            return fname

        log.info('Download data...')
        d = load_dataset("bavard/personachat_truecased", trust_remote_code=True)

        data = {'train': [], 'valid': []}

        for x in d['train'][:10000]:
            chat = {'utterances': []}

            h = x['history'] if type(x['history']) == list else []
            r = x['candidates'] if type(x['candidates']) == list else []
            h = h[:max_len]
            r = r[:max_len]

            if h and r:
                for i in range(len(h)):
                    if h[i]:
                        chat['utterances'].append({
                            'text': str(h[i]),
                            'speaker': 'user'
                        })
                    if i < len(r) and r[i]:
                        chat['utterances'].append({
                            'text': str(r[i]),
                            'speaker': 'assistant'
                        })

            if chat['utterances']:
                data['train'].append(chat)

        for x in d['validation'][:200]:
            chat = {'utterances': []}

            h = x['history'] if type(x['history']) == list else []
            r = x['candidates'] if type(x['candidates']) == list else []
            h = h[:max_len]
            r = r[:max_len]

            if h and r:
                for i in range(len(h)):
                    if h[i]:
                        chat['utterances'].append({
                            'text': str(h[i]),
                            'speaker': 'user'
                        })
                    if i < len(r) and r[i]:
                        chat['utterances'].append({
                            'text': str(r[i]),
                            'speaker': 'assistant'
                        })

            if chat['utterances']:
                data['valid'].append(chat)

        with open(fname, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        log.info(f'Completed: Training{len(data["train"])}Bar, verification{len(data["valid"])}Bar')

        # print
        if data['train']:
            log.info('\nexample:')
            for u in data['train'][0]['utterances'][:4]:
                log.info(f'{u["speaker"]}: {u["text"]}')

        return fname

    except Exception as e:
        log.error(f'error: {str(e)}')
        raise


def check_academic(msgs):
    keys = {
        'study', 'research', 'science', 'math', 'theory', 'experiment',
        'professor', 'student', 'university', 'college', 'academic',
        'paper', 'thesis', 'dissertation', 'course', 'lecture',
        'laboratory', 'exam', 'test', 'homework', 'assignment',
        'learn', 'education', 'school', 'class', 'teaching',
        'knowledge', 'book', 'library', 'study', 'learning'
    }

    txt = ' '.join(m['text'].lower() for m in msgs)
    return any(k in txt for k in keys)


def filter_academic(path):
    try:
        log.info('Start sifting through academic conversations...')

        with open(path, encoding='utf-8') as f:
            d = json.load(f)


        res = {
            'train': [x for x in d['train']
                      if check_academic(x['utterances'])][:500],
            'valid': [x for x in d['valid']
                      if check_academic(x['utterances'])][:100]
        }

        # 保存
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(res, f, ensure_ascii=False, indent=2)

        log.info(f'Completed: Training{len(res["train"])}Bar, verification{len(res["valid"])}Bar')
        return path

    except Exception as e:
        log.error(f'error: {str(e)}')
        raise


if __name__ == '__main__':
    p = get_data()
    filter_academic(p)
    log.info('Processing complete!')