# -*- coding: utf-8 -*-

import os.path
import sys

from xml.dom.minidom import parse

PATH = "tools"

def extract_requirements(args, dirname, names):

    no_requirements = []
    for name in names:
        path = os.path.join(dirname, name)
        if path.endswith(".xml"):
            dom = parse(path)
            tools = dom.getElementsByTagName("tool")
            for tool in tools:
                requirements = tool.getElementsByTagName("requirement")
                tool_name = tool.getAttribute("name")
                if len(requirements) > 0:
                    requirements = ", ".join(requirement.childNodes[0].data+("("+requirement.getAttribute("version")+")" if requirement.getAttribute("version") != "" else "")  for requirement in requirements)
                    print "%s : %s" % (tool_name, requirements)

def main():

    if len(sys.argv) != 2:
        print >> sys.stderr, 'usage: extract-requirements <galaxy_tools_path>'
        sys.exit(1)

    if not os.path.exists(sys.argv[1]):
        print >> sys.stderr, 'unknown path', sys.argv[1]
        sys.exit(1)

    os.path.walk(sys.argv[1], extract_requirements, None)