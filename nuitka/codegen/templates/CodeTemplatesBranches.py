#     Copyright 2012, Kay Hayen, mailto:kayhayen@gmx.de
#
#     Part of "Nuitka", an optimizing Python compiler that is compatible and
#     integrates with CPython, but also works on its own.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
""" Templates for conditional statements and expressions.

"""


template_branch_one = """\
if ( %(condition)s )
{
%(branch_code)s
}"""

template_branch_two = """\
if ( %(condition)s )
{
%(branch_yes_code)s
}
else
{
%(branch_no_code)s
}"""

template_conditional_expression = """\
( %(condition)s ? %(yes)s : %(no)s )"""