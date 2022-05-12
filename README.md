# Git-example

## 設定使用者名稱與信箱
```
$ git config --global user.name "Leo"
$ git config --global user.email "leo@gmail.com"

$ git config --list  #確認設定結果
```

## 初始化目錄

```
$ git init
```

## 查詢狀態
```
$ git status
```

## 添加檔案暫存區
```
$ git add test.html
$ git add *.html
$ git add --all
$ git add . # 舊版git(1.X) 不會處理刪除檔案，新版git跟--all相同
```
## 把暫存區的內容提交到倉庫裡存檔
* 不會將不在暫存區的檔案commit到儲存庫內，也就是需要先git add過的檔案才會處理
```
$ git commit -m "init commit" # -m "init commit" 對這次commit的敘述
```

## ⼯作區、暫存區與儲存庫

* 工作目錄 (working directory)
* git add 
* 暫存區 (staging area)
* git commit
* 儲存庫 (Repository)
```
$ git commit -a -m "update content"
```
* -a 只對在Repository內的檔案有效

## 檢查紀錄
```
$ git log
$ git log --oneline --graph #更精簡，更多commit，graph有圖片可以看分支及合併
$ git log --oneline --author="Sherly"
$ git log --oneline --author="Sherly\|Eddie"
$ git log --oneline --grep="WTF"
$ git log -S "Ruby" # 找commit 檔案內容有提到Ruby
$ git log --oneline --since="9am" --until="12am"
$ git log --oneline --since="9am" --until="12am" --after="2017-01"
```

## 刪除檔案
```
$ rm test.html # 刪除之後再git add
$ git rm test.html # 不用再add
$ git rm test.html --cached # --cached 不讓git再控管這個檔案，不會真的刪掉這個檔案
```

## 檔案改名
```
$ mv test.html world.html # delete and 新增檔案
$ git mv test.html world.html 
```

## 修改最後一個commit
```
$ git commit --amend -m "revise commit"
```

## 追加檔案到最近一個commit
```
$ git add cinderella.html
$ git commit --amend --no-edit # --no-edit 不要編輯commit訊息
```
* 修改跟追加盡量不要使用在已經push出去的commit

## 新增目錄
* 空目錄git是無法新增的，可以放置隨意的檔案，例如".keep", ".gitkeep"
```
$ touch images/.keep
```
## 隱藏檔案
[各種語言常見會忽略的檔案](https://github.com/github/gitignore)
```
$ touch .gitignore # 將要忽略的檔案加在裡面
```
* 在.gitignore存在之前的檔案不會被忽略，需要使用```git rm --cached```，將這些檔案移出git

## 清除檔案 clean
* 會清掉沒有被track的檔案
```
$ git clean #必須至少加上 -n -i -f
$ git clean -n # 查看那些檔案會被刪除，不會真的被刪
$ git clean -f # 強迫執行刪除當前目錄下所有沒有被track的檔案
$ git clean -i # 互動式刪除
$ git clean -d # 移除directories -x 連被ignored的檔案也會被移除 -X 只移除被忽略的檔案
```

## 檢視特定檔案的 Commit 紀錄
```
$ git log test.html # -p 可以查看修改了什麼
```
## 查看程式誰寫的
```
$ git blame test.html
$ git blame -L 5,10 index.html # 5~10行
```
## 找回刪掉的檔案
```
$ git checkout cinderella.html
$ git checkout .
$ git checkout HEAD~2 welcome.html # 找回距離現在兩個版本以前的welcome.html
```

## 拆掉commit
```
$ git reset e12d8ef^ # e12d8ef是SHA-1 ^代表前一次，^^兩次，五次以上會使用e12d8ef~5
$ git reset master^
$ git reset HEAD^
$ git reset 85e7e30 # 回到某個commit
```
## Reset
* ```--mixed``` 預設模式，把暫存區的檔案丟掉，工作目錄的檔案不變，commit拆出來的檔案會留在工作目錄 (在reset前的檔案會被保留下來，假設在reset前的改動，修改檔案或是刪除檔案，都會被保留在工作目錄中，也就是新的commit的動作都還在，只是分支指向commit的部分消失，要再將這些改動加到暫存區中)
* ```--soft```，暫存區及工作目錄檔案都不變，僅head改變，commit拆出來的檔案會放在暫存區
* ```--hard```，暫存區及工作目錄檔案都丟掉
```
$ git reset HEAD~2 # 我要前往兩個 Commit 之前的狀態
```
* 新的兩個commit還會在，只是暫時看不見
```
$ git reset e12d8ef --hard # 回到某個commit的SHA-1，即使已經reset
```
* 若不知道commit的SHA-1，可以使用Reflog查詢
```
$ git reflog
```
## HEAD
```
$ git branch
$ git checkout cat # 移到cat的branch
```
* HEAD會指向目前所在的分支

## 物件

* Blob 每個檔案會以Blob的形式儲存
* Tree 目錄以及檔案的檔名由Tree物件的方式存放，Tree會指向Blob(檔案，並記錄檔名)，或是另一個Tree(目錄)，
* Commit 紀錄Tree物件、commit的人、時間及訊息
* Tag 指向某個commit
* 在 Git 的世界裡，只要檔案的內容是⼀樣的，它們在 Git 的世界裡就會是同⼀顆 Blob 物件
1. Commit 物件會指向某個 Tree 物件
2. Tree 物件的內容會指向某個或某些 Blob 物件，或是其它的 Tree 物件
3. 除了第⼀個 Commit 物件以外，所有 Commit 物件都會指向它的前⼀次的 Commit 物件
4. Tag物件（Annotated Tag），指向某個Commit物件
5. 分支會指向某個Commit
6. HEAD會指向某個分支

```
$ git tag -a big_treasure -m "大祕寶"
```

## checkout

* 用來切換分支
```
$ git checkout master
$ git checkout -b sister # 若有分支則切換，沒有的話創建並切換
```
* 也可以用來找回檔案，可以指定commit的SHA-1，來找回特定版本的檔案，沒有指定的情況下，從```.git```中找回檔案的最新本，直接覆蓋工作區的檔案，並將有異動的部分加入暫存區中，原有的檔案被覆蓋以及暫存區(?)的檔案會消失，但如果檔案有commit上傳過，可以透過commit找回
* <font color="red">切換分支不會影響已經在工作目錄的修改? 但我自己實測沒有commit之前是不能切換分支(?)</font>
```
$ git checkout -b <branch> #可以同時建立和切換分支
```

## 分支

* 分支指向某個commit，master就是一個預設的分支，HEAD會指向一個分支，如果checkout某個commit，而那個commit沒有分支指著，就會發生detached HEAD，斷頭，在這個情況下還是可以add跟commit，不過之後比較不容易找回這個commit
* 若我直接跳到某個commit，就算他有分支指著，仍會斷頭?因為是指向commit?如果有分支的話要直接跳到分支比較好?
```
$ git branch # 印出專案所有分支，星號表示目前所在分支
$ git branch xxx 新增xxx分支
$ git branch -m xxx cat # 把分支xxx名字換成cat
$ git branch -d cat # 刪掉分支 -D強制刪除
$ git branch new_cat 6166cee # 建立一個叫做new_cat的分支，讓它指向6166cee這個commit
```
## rebase

* 另一種合併方式，但會修改歷史，不建議使用在push出去的commit上
* 有點像剪下貼上，但在過程中會產生新的commit
* 通常在還沒有push出去但感覺有點亂，或太瑣碎的commit，可以先使用rebase來整理完再推出去
```
$ git rebase dog
```
## ORIG_HEAD

* 在做危險操作以前git會有一個特別的紀錄點叫做```ORIG_HEAD```，會記錄危險操作之前HEAD的位置，例如合併或是Reset等等。
```
$ git reset ORIG_HEAD --hard
```
## 合併發生衝突

* 找到衝突檔案，把衝突的部分修改掉，加到暫存區後commit
* rebase用同樣的方法，修改完檔案後加到暫存區，執行```$ git rebase --continue```繼續合併
* 若是其他檔案，如jpg，使用git checkout來決定使用哪個分支的檔案
```
$ git checkout --ours cute_animal.jpg  # 使用我們的檔案
$ git checkout --theirs cute_animal.jpg # 使用他們的檔案 
```

## 修改歷史訊息

* Rebase 指令的互動模式
```
$ git rebase -i bb0c9c2
# p, pick = use commit
# r, reword = use commit, but edit the commit message
# e, edit = use commit, but stop for amending
# s, squash = use commit, but meld into previous commit
# f, fixup = like "squash", but discard this commit's log message
# x, exec = run command (the rest of the line) using shell
# d, drop = remove commit
```
* 修改前面的command，可以決定每個commit該怎麼做
* reward可以修改commit訊息，但會導致所有的commit重建，因為名字改變，SHA-1也改變
* squash 融合commit
* edit可以把commit拆成多個commit，或是在commit之間新增commit，將想要修改的commit改為edit後，等停在該commit時，利用reset拆掉commit
* 分別使用add以及commit來拆開commit
* 結束後，rebase --continue
```
$ git reset HEAD^
```
* 修改commit順序，只要在rebase頁面中修改commit的順序即可
* 刪除commit 使用drop，或是直接刪掉某行

## Revert
```
$ git revert HEAD --no-edit
```
* 把最後一次commit的內容刪掉，不過會新增一個新的commit表示刪掉了那個commit
* 若要取消可以再使用一個revert來revert剛剛的commit
```
$ git revert HEAD --no-edit
$ git reset HEAD^ --hard #或是使用reset
```
* 在團隊合作中無法使用reset，使用revert來取消commit，並不會修改歷史，而是新增commit來取消原有commit的內容

## 標籤

* 版本號
* 輕量標籤 （lightweight tag）
* 附註標籤 （annotated tag）
```
# 輕量標籤
$ git tag big_cats 51d54ff # 在51d54ff的commit上貼上big_cats的標籤
# 有附註標籤
$ git tag big_cats 51d54ff -a -m "Big Cats are comming" # -a代表建立有附註的標籤
$ git show big_cats # 顯示tag的訊息
$ git tag -d big_cats # 刪除標籤
```
* tag跟分支很像，只是tag不會隨著commit移動

## 工作到一半，林時切換到其他任務
* 先commit，之後再reset
```
$ git add --all
$ git commit -m "not finish yet"
$ git reset HEAD^
```
* 或是使用stash
```
$ git stash
$ git stash pop stash@{2} # 拿回剛剛存起來的東西，並刪掉該stash
$ git stash apply stash@{0} # 拿回東西，但不刪掉stash
```
## filter-branch
* 想要刪掉某些東西，但已經commit很多了
```
$ git filter-branch --tree-filter "rm -f config/database.yml" # checkout到每個commit的時候執行指定的指令，執行完後自動重新commit，這裡的例子是刪掉database.yml這個檔案
```
* 後悔執行filter-branch
```
$ git reset refs/original/refs/heads/master --hard
```
## 把檔案從git內真正刪除

* 把檔案所在的commit內刪掉
* 把可能有的備份點給刪除
* Reflog也需要清除
* 在叫垃圾車回收，記得要加上--prune=now，否則還是要等時間到才會載走
```
$ git filter-branch -f --tree-filter "rm -f config/database.yml" # -f 強制覆寫filter-branch的備份點
$ rm .git/refs/original/refs/heads/master # 把備份點給刪掉，避免跳回去
```
* Reflog也要清掉
```
$ git reflog expire --all --expire=now # 使Reflog立即過期，而非等30天後
$ git fsck --unreachable # 檢查物件是否有效，以及有沒有連接，後面unreachable表示查看無法到達的物件
$ git gc --prune=now # 把無法到達的物件回收
```

## cherry-pick
* 撿別的分支的某些commit過來合併
```
$ git cherry-pick 6a498ec
```
* 一次撿好幾個
```
$ git cherry-pick fd23e1c 6a498ec f4f4442
```
* 撿過來但先不合併
```
$ git cherry-pick 6a498ec --no-commit
```
## GitHub

* 先在github上新增新的repository
* 接著在本地新增節點，用origin代稱GitHub服務器位置
```
$ git remote add origin git@github.com:kaochenlong/practice-git.git
$ git push -u origin master
```
* 把master這個分支推向origin這個位置
* 若master不存在就建立一個叫做master的同名分支
* 如果存在的話就移動到server上，並指向最新的進度
* ```-u``` upstream，上游，其實就是另一個分支的名字，在git中，每個分支可以設定一個上游，但每個分支最多只能設定一個upstream，他會指向並追蹤某個分支
* 使用了```-u```，下次就可以直接```git push```，而不用每次都```git push origin master```


```
$ git push origin master
$ git push origin master:master # 與上面相同，把本地的master分支推上server的master更新進度
$ git push origin master:cat # 推上server上的進度，建立或更新一個叫做```cat```的分支
```
## Pull

```
$ git fetch # 把server上的進度拉下來
$ git merge origin/master # 拉下來的進度為origin/master，可以把它看成本地master分出去的分支，所以利用merge來進行合併
$ git pull --rebase # 利用rebase來合併，避免產生新的commit
```
> git pull = git fetch + git merge
## Push失敗
* 進度與server上不同
* 先拉再推
* 把server上的進度拉下來合併後再push
```
$ git pull --rebase
```
* 強制push
* 但會覆蓋掉前面的進度，不推薦
```
git push -f # 或是--force
```
## Clone
```
$ git clone git@github.com:kaochenlong/dummy-git.git
$ git clone git@github.com:kaochenlong/dummy-git.git hello_kitty # 改名成hello_kitty
```
## Pull Request (PR)
* 先複製，分叉(fork)
* 修改 + Push回自己帳號
* 發request
* 作者同意後merge
## 跟上fork專案的進度
* 砍掉重練，把fork過來的專案砍掉，再重新fork一次
* 跟上游同步
* 在fork來的專案上新增節點
* 利用fetch抓取原作專案的內容，接著merge到自己這邊的專案上
## 刪除遠端分支
* 利用網頁，branch的地方有個垃圾桶來刪除
* 或是利用push來刪除，使用空的內容來刪除遠端分支
```
$ git push origin :cat # 刪除cat分支
```
## git push -f
* 在使用Rebase整理commit後，修改了已經發生的事實，所以正常來說是推不上去的，所以使用force push來解決這個問題，使用前請知會同專案的隊友
* 可以將force用在自己使用的分支上，來整理commit，因為他也只會影響到這個分支，不會影響到他人
* Github可以設置防止force某些分支
* 救回資料，找到擁有舊資料的其他人，使用```git push -f```，覆蓋掉新的內容，把正確的推上去
## 更新檔
* 取得某次commit後到某個commit的更新檔
```
$ git format-patch fd7cd38..6e6ed76
$ git format-patch -2 # 產生最新兩次commit的更新檔
$ git format-patch -2 -o /tmp/patches # -o 指定更新檔位置
```
* 使用更新檔
```
$ git am /tmp/patches/*
```
## Git Flow
```
```
```
```

