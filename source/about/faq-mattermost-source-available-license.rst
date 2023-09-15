:orphan:

Mattermost Source Available License questions
=============================================

.. contents:: On this page
    :backlinks: top
    :depth: 2

What is the Mattermost Source Available License?
------------------------------------------------

A source available license gives access to source code, but places restrictions on its use. The Mattermost Source Available License allows free-of-charge and unrestricted use of the source code in development and testing environments, but requires a valid Mattermost Enterprise Edition License in a production environment.

How can I identify code licensed as source available?
-----------------------------------------------------

When the Mattermost Source Available ``LICENSE`` file appears at the root of a repository, the restrictions apply to all source code within the repository. A note in the ``README.md`` often identifies the use of this license and links to this FAQ.

When the Mattermost Source Available ``LICENSE`` file appears in a specific directory, the restrictions apply to all source code within that directory. This directory is often called "enterprise". For additional clarity, an additional ``LICENSE.enterprise`` file may appear in the root directory, symlinked to the ``enterprise/LICENSE`` file.

In all cases, any third party components remain licensed under their original license.

An example directory layout, using an Enterprise license, is shown below:

.. image:: ../images/source-available-license.png
   :alt: An example directory layout shows how Enterprise subscription plan restrictions apply to Mattermost source code based on where the Mattermost Source Available license file appears in the Mattermost deployment directory.
Why are you changing the licensing model?
-----------------------------------------

Our plugin framework delivers substantial value to our enterprise customers but requires significant development and support resources. This change to the licensing model allows us to continue developing open source features while selectively charging for features.

How are repositories changing?
------------------------------

As we add enterprise-only functionality, we will update the license on affected Mattermost-authored plugin repositories. The intent is to work alongside the existing, open source functionality in our plugins while reserving certain enterprise functionality to customers who pay us for enterprise licenses.

To which repositories does this apply?
--------------------------------------

We plan to apply this license to the enterprise directories of our `Jira <https://github.com/mattermost/mattermost-plugin-jira>`__, `Microsoft Calendar <https://github.com/mattermost/mattermost-plugin-mscalendar>`__, and `Microsoft Teams Meetings <https://github.com/mattermost/mattermost-plugin-msteams-meetings>`__ plugins. We also intend to release `Playbooks </guides/repeatable-processes.html>`__ and `Channel Export <https://github.com/mattermost/mattermost-plugin-channel-export>`__ plugins under the Mattermost Source Available License. New, Mattermost-authored plugins will generally be released under the Mattermost Source Available License. When we update the licenses, we will release a new version and note the change in the ``README.md`` file of the GitHub repository and any release notes.

We expect to keep plugins without an enterprise component under our open source license. No licensing changes are planned to non-plugin repositories, such as `mattermost <https://github.com/mattermost/mattermost>`__ or `mattermost webapp <https://github.com/mattermost/mattermost/tree/master/webapp>`__.

Will the repositories be public?
--------------------------------

Yes, existing repositories will stay public. We are now also able to make public several enterprise-only plugins under the Mattermost Source Available License previously developed in private.

Can I still contribute?
-----------------------

Yes, we continue to welcome all contributions. Mattermost may select some contributions as enterprise features and license them under the Mattermost Source Available License. We will aim to communicate such decisions as early as possible in the contribution process.

As with all Mattermost repositories, you will still need to sign the `Mattermost CLA <https://mattermost.com/contribute/>`__. We will not accept contributions without signing the Mattermost CLA.

Do I need to re-sign the `Mattermost CLA <https://mattermost.com/contribute/>`__?
-------------------------------------------------------------------------------------------------------

No, if you have already signed the `Mattermost CLA <https://mattermost.com/contribute/>`__, you do not need to sign it again.

Can I compile your plugins by myself?
-------------------------------------

Yes. If you have a Mattermost Enterprise Edition license, you are free to compile and use a plugin under the Mattermost Source Available License. Furthermore, if you are developing against or testing with such a plugin, you are free to compile and test a plugin even without a Mattermost Enterprise Edition license. Without an Enterprise Edition license, source available plugins may have reduced functionality or refuse to start altogether. Request a `trial license <https://mattermost.com/trial/>`__ if your testing requires access to enterprise functionality.

Several of our customers value complete access to our source code and compile our plugins from source before deploying to their production servers. By adopting the Mattermost Source Available License, we can develop enterprise-only features in public without impacting this workflow.

Will you distribute open source plugin binaries without any licensing restrictions?
-----------------------------------------------------------------------------------

At this time, we have no plans to distribute more than one version of each of our plugins. Without a Mattermost Enterprise Edition License, plugins may have reduced functionality or refuse to start altogether.

Can I continue to use the existing open source repositories without restriction?
---------------------------------------------------------------------------------

Yes, the Mattermost Source Available License will only apply from the date it is added and to the versions in which it is included.

Do I need to use the Mattermost Source Available License for plugins I create?
------------------------------------------------------------------------------

You are free to license your own code as you see fit. We will not apply the Mattermost Source Available License either to the `starter-template <https://github.com/mattermost/mattermost-plugin-starter-template>`__ or `demo <https://github.com/mattermost/mattermost-plugin-demo>`__ plugins, leaving them under a permissive open source license to give you the freedom to develop your own plugins.

Can I publish my own plugin and rely on enterprise specific functionality?
--------------------------------------------------------------------------

As before, you are free to license your own code as you see fit. Note that some server functionality is only enabled with a Mattermost Enterprise license regardless of how you license your plugin.

Can’t someone compile out any license restrictions?
---------------------------------------------------

We trust our community to honor the Mattermost Source Available License and work alongside us to develop features across our free and paid offerings. Our Support team does not provide support to unlicensed, enterprise-only functionality.

If I make my own plugin using your source available code, can I remove the license restriction?
------------------------------------------------------------------------------------------------

No, the Mattermost Source Available License continues to apply to modifications.

Will you pursue legal action if this license is violated?
---------------------------------------------------------

Yes, if necessary. But we would always rather collaborate, so if you need to negotiate a different license, please ask us.

Is this a legal document?
-------------------------

No. This FAQ is informational only. The Mattermost Source Available License stands on its own, and this FAQ does not affect its meaning.

What is the full text of the Mattermost Source Available License?
-----------------------------------------------------------------

"The Mattermost Source Available License (the “Source Available License”)
(c) Mattermost, Inc. 2015-present.

With regard to the Mattermost Software:

This software and associated documentation files (the "Software") may only be
used in production, if you (and any entity that you represent) have agreed to,
and are in compliance with all of the following: (a) the Mattermost Terms of Use, 
available at https://mattermost.com/terms-of-use/ (the "TOU"), (b) and the Mattermost 
Software License Agreement,  available at https://mattermost.com/enterprise-edition-terms/ 
(the “SLA”) or other licensing agreement governing your use of the Software, as agreed 
by you and Mattermost, and otherwise have a valid Mattermost Enterprise for the correct 
number of Registered Authorized Users the Software. Subject to the foregoing, you are free
to modify this Software and publish patches to the Software. You agree that
Mattermost and/or its licensors (as applicable) retain all right, title and
interest in and to all such modifications and/or patches, and all such
modifications and/or patches may only be used, copied, modified, displayed,
distributed, or otherwise exploited with a valid license or Subscription for the correct number of 
Registered Authorized Users of the Software.  Notwithstanding
the foregoing, you may copy and modify the Software for development and testing
purposes, without requiring a valid license or Subscription.  You agree that Mattermost and/or
its licensors (as applicable) retain all right, title and interest in and to
all such modifications.  You are not granted any other rights beyond what is
expressly stated herein.  Subject to the foregoing, it is forbidden to copy,
merge, publish, distribute, sublicense, and/or sell the Software.

The full text of this Source Available License shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

For all third party components incorporated into the Mattermost Software, those
components are licensed under the original license provided by the owner of the
applicable component."
