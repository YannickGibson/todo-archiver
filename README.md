# Markdown Todo Archiver
Minimal workflow for managing TODO items. 
## Workflow

[todoa.md](todoa.md) ⬇️

```md
# 📆 TODO's

## 🔁 Daily Tasks
- [ ] Drink 2L water  
- [x] Go for a 30 min walk  
- [ ] Read 20 pages  

## 📆 Weekly Tasks
- [x] Write project report draft  
- [ ] Attend weekly sync meeting  
- [ ] Clean workspace  

## 🎯 Internship Tasks
- [ ] Finish feature implementation  
- [x] Submit PR for bug fix  
- [ ] Review mentor’s feedback  

## ❓ Questions
- [ ] Ask mentor about deployment process  
- [x] Clarify project deadline  
```

Run `python todo_archiver.py` (set it to run daily).

[completed.md](completed.md) ⬇️
```md
# ✅ Completed TODO's


## Daily Tasks
- [x] (2025-09-13) Go for a 30 min walk  


## Weekly Tasks
- [x] (2025-09-13) Write project report draft  


## Internship Tasks
- [x] (2025-09-13) Submit PR for bug fix  


## Questions
- [x] (2025-09-13) Clarify project deadline  
```
[todoa.md](todoa.md) ⬇️
```md
# 📆 TODO's

## 🔁 Daily Tasks
- [ ] Drink 2L water  
- [ ] Read 20 pages  

## 📆 Weekly Tasks
- [ ] Attend weekly sync meeting  
- [ ] Clean workspace  

## 🎯 Internship Tasks
- [ ] Finish feature implementation  
- [ ] Review mentor’s feedback  

## ❓ Questions
- [ ] Ask mentor about deployment process  
```

You can also check [merge.md](merge.md) for all tasks.

# Setup
Have Python 3.10+ installed. No other dependencies needed.
# Additional usage
## Reset todo
- Removes all current tasks and history of completed tasks.

Consult [constants.py](constants.py) to choose your own headings.

To execute it run `make reset` or run `reset.py` directly and then delete `archive` folder.

## Delete archive
-  Removes all history of completed tasks.

To execute it run `make delete` or remove `archive` folder.

# Bonus tip
On Windows you can use Everything app and search `todoa` to quickly find the TODO file.