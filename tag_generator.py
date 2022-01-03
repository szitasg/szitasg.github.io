#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import os
import yaml


class TagGenerator(object):

    POST_DIR = '_posts/'
    TAG_DIR = 'public/tag/'
    TAG_TEMPLATE = '---\nlayout: tag\ntitle: %s\ntag:\n  name: %s\n  url: %s\nrobots: noindex\n---\n'

    def __init__(self):
        if not os.path.exists(self.TAG_DIR):
            os.makedirs(self.TAG_DIR)

        self.cleanup_old_tags()
        self.generate()

    def cleanup_old_tags(self):
        for tag in glob.glob(self.TAG_DIR + '*.md'):
            os.remove(tag)

    def generate(self):
        tags = list()

        for post in glob.glob('%s*md' % self.POST_DIR):
            with open(post, 'r', encoding='utf8') as post_file:
                yaml_content = post_file.read().split('---')[1]
                yaml_content = yaml.safe_load(yaml_content)
                for tag in yaml_content['tags']:
                    if tag not in tags:
                        tags.append(tag)

        for tag in tags:
            with open('%s%s.md' % (self.TAG_DIR, tag['url']), 'a', encoding='utf8') as tag_file:
                tag_file.write(self.TAG_TEMPLATE % (tag['name'], tag['name'], tag['url']))


if __name__ == '__main__':
    TagGenerator()
