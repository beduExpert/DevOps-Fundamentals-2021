
# Git Flow #

<span style="color:grey"> <ins>Prerequsitos:</ins> </span>


### Tener instalado GitFlow ###
</br>

Pasos para instalar dependiendo tu plataforma:


- Equipos MacOS X

</br>

~~~

brew install git-flow

~~~

</br>

- Linux

</br>

~~~

apt-get install git-flow

~~~
</br>

- Windows


</br>

~~~

wget -q -O - --no-check-certificate https://github.com/nvie/gitflow/raw/develop/contrib/gitflow-installer.sh | bash

~~~
</br>


## Pasos: ##
---
</br> 

### 1.- Vamos a iniciar un repositorio en nuestro local: ###


*`git init `*
~~~ 
# git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint:
hint: 	git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint: 	git branch -m <name>
Initialized empty Git repository in beduRepoGitFlow/.git/
~~~
</br>


### 2.- Iniciamos nuestro git flow con: ###



`git flow init`
</br>

~~~

# git flow init

No branches exist yet. Base branches must be created now.
Branch name for production releases: [master]
Branch name for "next release" development: [develop]

How to name your supporting branch prefixes?
Feature branches? [feature/]
Release branches? [release/]
Hotfix branches? [hotfix/]
Support branches? [support/]
Version tag prefix? []
~~~
</br>



### 3.- Creación de una rama de fusión: ###


`git flow feature start feature_branch`
</br>

~~~
# git flow feature start feature_branch

Switched to a new branch 'feature/feature_branch'

Summary of actions:
- A new branch 'feature/feature_branch' was created, based on 'develop'
- You are now on branch 'feature/feature_branch'

Now, start committing on your feature. When done, use:

     git flow feature finish feature_branch

~~~

</br>

### Nota: Seguiremos usando git de forma normal
---

</br>

### 4.- Finalización de una rama de fusión: ###
`git flow feature finish feature_branch`
</br>

~~~
# git flow feature finish feature_branch

Switched to branch 'develop'
Already up to date.
Deleted branch feature/feature_branch (was 22d1fa0).

Summary of actions:
- The feature branch 'feature/feature_branch' was merged into 'develop'
- Feature branch 'feature/feature_branch' has been removed
- You are now on branch 'develop'

~~~
</br>

### Nota: Esta rama deberá ser eliminada una vez que hayan terminado de trabajar en ella. ###
---
</br>

### 5.- Publicación de una Rama ###

`git flow release start 0.1.0`

</br>

~~~
# git flow release start 0.1.0
Switched to a new branch 'release/0.1.0'

Summary of actions:
- A new branch 'release/0.1.0' was created, based on 'develop'
- You are now on branch 'release/0.1.0'

Follow-up actions:
- Bump the version number now!
- Start committing last-minute fixes in preparing your release
- When done, run:

     git flow release finish '0.1.0'

~~~

</br>

### 6.- Finalizar una rama: ###

`git flow release finish '0.1.0'`

</br>

~~~
# git flow release finish '0.1.0'
Switched to branch 'master'
Deleted branch release/0.1.0 (was 22d1fa0).

Summary of actions:
- Latest objects have been fetched from 'origin'
- Release branch has been merged into 'master'
- The release was tagged '0.1.0'
- Release branch has been back-merged into 'develop'
- Release branch 'release/0.1.0' has been deleted

Nota: No olvidar agregar un comentario en esta última sentencia, de lo contrario obtendremos la siguiente leyenda:

# git flow release finish '0.1.0'
fatal: no tag message?
Tagging failed. Please run finish again to retry.
~~~
</br>