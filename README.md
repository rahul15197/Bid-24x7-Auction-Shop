# Bid-24x7-Auction-Shop
Bid 24x7 is an auctioning platform developed in python, and GUI is implemented with the help of Tkinter library. For Database management SQLite3 has been used.

# Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Features](#features)
- [Installation](#installation)
- [Working](#working)
- [Contributions](#contributions)


## Introduction
Bid 24x7 is a platform independent GUI based auctioning system which aims to provide an efficient platform for the users to bid/list items of different categories. It is a multi-user platform which aims to provide a common robust platform for item auctions.

For Database management SQLite3 has been used to get better and fast Database connectivity and management.

There are two views in Bid 24x7: -
1. User view : In user view, user can be bidder or seller. User can bid/sell items from the Bid 24x7.
2. Admin View : Admin view is basically a view with extra privileges given to the administrator for managing categories, blocking fraudelent users, bill generation and etc.

## Requirements
python - version 3.7.4 or above
SQLite - version 3
Tkinter - For GUI
Reportlab - For geenrating bill

## Features
1. Full GUI based Auctioning desktop application.
2. Login and registration for users and admin with complete validations.
3. Add new item to list for auction with user defined initial bid and timestamp.
4. Buyer can bid for the items if available for the sale only if bid amount is higher than the previous/initial bid.
5. Fraudlent user detection and blocking them completely from the platform so as to prevent them from re-registration.
6. Admin can add new categories,merge two categories,delete of existing categories.

## Installation
```bash
python master.py
```

- register using valid credentials
- login with registered id to start using Bid 24x7

## Working
For a detailed working process, please refer to the Report file.

## Contributions
Project was created by [Rahul Maheshwari](mailto:rahul19027@iiitd.ac.in) and [Abhishek Singh Chouhan](mailto:abhishek19085@iiitd.ac.in) - feel free to contact us!!
