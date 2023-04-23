# sc1015
SC1015 group project

## How to get started
prerequisite: Need to understand how to use:
- windows: command prompt or powershell or [git bash](https://git-scm.com/downloads) or [Github Desktop](https://desktop.github.com/) (**RECOMMENDED!!!** Simple to use, no need to use terminal such as command prompt, powershell, bash and etc. Can step the steps below)
- linux: bash or any other terminal

### Steps:
1. create a ssh key (you can only do a git clone/pull/rebase/fetch using ssh method)
follow this [guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) to generate ssh key on your machine/laptop

2. add the ssh key into your github account. If you dont add the newly generated ssh key into your account, github will never recognize your account. Follow this [guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) on how to add ssh key into your github account

3. do a test on SSH connection by follow the following [guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection)


Once the above setups are done, you can do git clone of this repository. One thing you may want to take note is to ensure that you are at the intended working directory [windows](https://www3.ntu.edu.sg/home/ehchua/programming/howto/CMD_Survival.htmlm) or [linux](https://www.cyberciti.biz/faq/how-to-change-directory-in-linux-terminal/) before doing a git clone.

To do a git clone of the repository, you can enter the following command:
```
ssh git@github.com:Amizzuddin/sc1015.git
```
you sould have all the contents of the repository.

## How to contribute

1. install [miniconda3](https://docs.conda.io/en/latest/miniconda.html) on your machine. You can follow this [user guide](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#installing-conda-on-a-system-that-has-other-python-installations-or-packages) on how to get the installation done on your local machine

2. make sure you are in the base environment. An example will be as the following ![screenshot](images/conda_base_environment.png)
once verified, run the following command (line starts with # are comments)
```
# add conda-forge as one of the channels
conda config --env --add channels conda-forge

# install mamba (once install, you can replace conda to mamba for commands. They are the same but mamba have better logging as compared to conda)
conda install mamba -c conda-forge

# install mamba bash completion (you dont have to type everything, you can type a little andpress the 'tab' butto on your keybopard to auto complete the command! nice feature right?)
mamba install mamba-bash-completion

# create a new environment for this project. You wont want your dependencies affecting other python projects. This is the beauty of working in conda environment!
mamba create env --name <the name of your new environment for the project> python=3.9

# finally install the dependencies 
# [IMPORTANT] in order to run main.ipynb (due to dependencies to other .ipynb files)
mamba install --file requirements.txt

```

3. finally create a branch so that all of us can work parallel. **No one should be working on main branch!**. main branch is used for testing the integration of our codes and will be use as the finalize code for project submission. you can follow the following [create & delete branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository)

4. any merging of code from your branch to the main branch, you can do a pull request. Follow the following guide on [create a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) and make sure to add team members as [reviewers](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/requesting-a-pull-request-review) before merging can be done

5. Contributions should be placed under "contributions" folder. If you feel your function may come handy, please create a call function and add them into "common/function.ipynb"

## Some other informations
You will often need to [commit](https://github.com/git-guides/git-commit), [push](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository), [rebase](https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase) and [pull](https://www.atlassian.com/git/tutorials/syncing/git-pull)


## Finally
Happy working with you guys. Hope this project will give you a view how programmers work in the industries as well. I know we are students but this are meant to make our life easy at collaborating. I know the probelms with onedrive and google drive and I agree github address this collaboration issues.
