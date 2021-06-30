# Accessing GitHub with Key

### Procedure

0. We want to sync our command line (where we run git) with GitHub. The goal is to get our code into the **mycode** repo we created. Move to the **~/.ssh** home directory.

    `student@bchd:~$` `cd /home/student/.ssh`

0. Now we will generate a new RSA keypair. We will use this to communicate securely with GitHub because as of August 2021, GitHub will no longer accept passwords from us. This will generate two files, the private key (**id_rsa_github**) and the public key (**id_rsa_github.pub**).

    `student@bchd:~/.ssh$` `ssh-keygen -f id_rsa_github`

    ```
    Generating public/private rsa key pair.
    Enter passphrase (empty for no passphrase):
    ```

    > When you see this, you will need to hit enter twice

    ```
    Enter same passphrase again:
    Your identification has been saved in id_rsa_github.
    Your public key has been saved in id_rsa_github.pub.
    The key fingerprint is:
    SHA256:DFjw7WCP+u2luMtPATqKHGBi/+XNUzlRYfqIYz8S2/Q student@bchd
    The key's randomart image is:
    +---[RSA 2048]----+
    |    ...      +.  |
    |     + .    +    |
    |oo  . * .  o     |
    |= .  o O  . =    |
    | . .o ..S= * .   |
    |.....oo +.O o    |
    |... .. ..*.+ E   |
    |     o + oo .    |
    |      *==        |
    +----[SHA256]-----+
    ```

0. Next we need to copy the text from inside of the **id_rsa_github.pub** public key into our clipboard. We will need to paste this into GitHub soon.

    `student@bchd:~/.ssh$` `cat id_rsa_github.pub`

    ```
    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCvTemj7NIlxXEu97VyN4wcmob+F0wQ0nPinZSdUvlWSGAx790EmfXmckZ01/aFDOKIA4OZWYtW95DaGqQ+Tja3QUYlAdTdIlp4TTgH3ZE+KdaLc16rN9FzHv8hwdLFx8CugNw/u/sDbYjEM1qlazB5fbAf0LZ+mN5iCDn6IaYbPZ0wQdF9s4RI/z5wS5wE/J++KV/xJA0f2ICZwaKj4Kq/fron2KoYRkCYcma0oHYvVSnnuxCVGbOJdhWK1LiJRPweNUajp0OItECJxgCR1gB/DVEWnBmknOcPnY6q3QeaUrm28nPSAjGTkfFSHDbOJptaqKaSkRhwNsuOGiw6KQ1R student@bchd
    ```

    > Select all of the output and copy it. NOTE: Yours will be different than the one listed above!

    **RETURN TO GITHUB NOW**

0. At the top of the screen, click on your username to return to your homepage.

0. You should see your repository `mycode-dev`. Click into it.

0. Near the top right of the screen, there is a little gear icon that says **Settings**. Click on that.

0. On the left of the screen, click on **Deploy Keys**. Deploy keys are essentially a token that we set up that allow somebody to read from, and optionally write to, our repository, even if it is private. They just need to have the private key set up on their system as a means of authenticating with the public key stored on github.

0. Your screen should look like the following. Click on the button that says **Add deploy key**.

    ![deploy key](https://static.alta3.com/courses/microservices/deploy_key_02.png)

0. Give your key a name. **alta3 environment** would work. Then paste your key (from **id_rsa_github.pub**) into the large text box. And also click on the checkbox that says **Allow write access**. Then, click **Add key**.

    ![deploy key pt 2](https://static.alta3.com/courses/microservices/deploy_key_03.png)

## Other Useful Resources

- If you ever run into a problem using git / GitHub, let the instructor know. It is critical to start learning to version control code. You might want to spend some time clicking around on the following guides. They're quite short, and although you might not understand what they're talking about, they'll begin exposing you to the way we 'speak' when using git & version controlling software. Some getting started guides relating to GitHub can be found here: <a href="https://guides.github.com/" target="_blank">https://guides.github.com/</a>

- Windows and Mac users might also check out the local client GitHub Desktop, available at <a href="https://desktop.github.com/" target="_blank">https://desktop.github.com/</a> This client makes it **easy** to work through git via a local GUI on your Windows or Mac desktop environment.

<br><br><div align="center">

![Alta3 Logo](https://static.alta3.com/images/Alta3-logo_large.png)

</div>
