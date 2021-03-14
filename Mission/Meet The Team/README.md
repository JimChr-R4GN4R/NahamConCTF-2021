After a while, I Checked the hints:

HINT: "Can we please stop sharing our version control software out on our website?"

HINT AGAIN: you are looking for a publicly accessible version control software folder published on the constellations.page website itself 



So searched on google 'version control software folder ctf'


and found this: https://blog.jakubjuszczak.de/writeup-ctf-0x00sec-web-exercise-1/

Checked https://constellations.page/.git
and it was forbidden!
So I decided to follow his instructions to retrieve the git commits!


So downloaded GitTools and then:
./gitdumper.sh https://exercise-1.0x00sec.dev/.git/ output
Then got in `output` folder and firstly typed:
`git status` to see the deleted files.

Got nothing useful and then decided to use `git log`
which also hasn't something useful.

Then used `git show` to check the history and got this:
```
Author: Leo Rison <leo.rison@constellations.page>
Date:   Tue Feb 23 19:20:14 2021 -0500

    Management said I need to remove the team details so I redacted that page and added it to robots.txt

diff --git a/meet-the-team.html b/meet-the-team.html
index 8257067..aafa3bc 100644
--- a/meet-the-team.html
+++ b/meet-the-team.html
@@ -61,10 +61,12 @@
                <div class="container">
                        <div class="row">
                                <div class="col-lg-8 mx-auto">
-                                       <h2 class="text-white mb-4">Meet The Team</h2>
-                                       <p class="text-white-50">
+                                       <h2 class="text-white mb-4"><span style="color:red">Redacted</span></h2>
+                                       <p class="text-white-50" >

-                                               Want to know about the brains behind the operations? Get to our know team members on socials! #teamwork
+                                               <span style="color:red">Sorry, for security reasons our team has decided to no longer publicize employee names and info.</span>
+
+                                       </p>

                                </div>
                        </div>
@@ -72,33 +74,6 @@
                </div>
        </section>

-       <!-- Projects Section -->
-       <section id="projects" class="projects-section bg-light">
-               <div class="container">
-
-                       <ul>
-                               <li><h4><b>Orion Morra</b> &mdash; Support</h4></li>
-
-                               <li><h4><b>Lyra Patte</b> &mdash; Marketing</h4></li>
-
-                               <li><h4><b>Leo Rison</b> &mdash; Development</h4></li>
-
-                               <li><h4><b>Gemini Coley</b> &mdash; Operations</h4></li>
-
-                               <li><h4><b>Hercules Scoxland</b> &mdash; Sales</h4></li>
-
-                               <li><h4><b>Vela Leray</b> &mdash; Management</h4></li>
-
-                               <li><h4><b>Pavo Welly</b> &mdash; HR</h4></li>
-
-                               <li><h4><b>Gus Rodry</b> &mdash; Accounting</h4></li>
-
-                               <!-- <li><h4><b>flag{4063962f3a52f923ddb4411c139dd24c}</b></h4></li> -->
-
-                       </ul>
-               </div>
-       </section>
-


        <!-- Contact Section -->
diff --git a/robots.txt b/robots.txt
new file mode 100644
index 0000000..f100d92
--- /dev/null
+++ b/robots.txt
@@ -0,0 +1,4 @@
+User-agent: *
```

And got the flag!


Flag: flag{4063962f3a52f923ddb4411c139dd24c}