B
    CC�]2  �            
   @   s$  d dl mZ d dlmZ d dlmZ d dlZd dlZd dlZd dl	Z	d dl
Z
dZdZdZdd	� Ze�� Ze�d
� y4ed d Zed d Zed d Zeeee�ZW n: ek
r�   e�d� e�  eed � e�d� Y nX e��  e�� �s&e�e� e�d� e�  e�eeed e �� e�d� e�  g ZdZ dZ!g Z"eee d e� e!d d��Z#e�$e#j� x:eD ]2Z%ye%j&dk�r�e"�'e%� W n   �wpY nX �qpW eed e � d Z(x<e"D ]4Z)eed e e*e(� d d e)j+ � e(d7 Z(�q�W ed� eed e �Z,e"e-e,� Z.eed � e
�/d� g Z0ej1e.dd�Z0eed � e
�/d� e2dd d!d"���Z3e	j4e3d#d$d%�Z4e4�5d&d'd(d)d*d+g� xxe0D ]pZ6e6j7�r�e6j7Z7ndZ7e6j8�r�e6j8Z8ndZ8e6j9�r�e6j9Z9ndZ9e8d, e9 �:� Z;e4�5e7e6j<e6j=e;e.j+e.j<g� �q�W W dQ R X eed- � dS ).�    )�TelegramClient)�GetDialogsRequest)�InputPeerEmptyNz[1;31mz[1;32mz[1;36mc               C   sV   t dt� dt� dt� dt� dt� dt� dt� dt� d	t� d
t� dt� dt� d�� d S )N�
u	   ╔╦╗u   ┌─┐┬  ┌─┐u   ╔═╗  ╔═╗u7   ┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
u    ║ u   ├┤ │  ├┤ u   ║ ╦  ╚═╗u1   │  ├┬┘├─┤├─┘├┤ ├┬┘
u    ╩ u   └─┘┴─┘└─┘u   ╚═╝  ╚═╝ur   └─┘┴└─┴ ┴┴  └─┘┴└─

            version : 1.0
        youtube.com/theunknon
        )�print�re�cy� r	   r	   �teleg-scrapr.py�banner   s    r   zconfig.dataZcred�id�hash�phone�clearz"[!] run python3 setup.py first !!
�   z[+] Enter the code: ��   )Zoffset_dateZ	offset_idZoffset_peer�limitr   Tz&[+] Choose a group to scrape members :�[�]z - � z[+] Enter a Number : z[+] Fetching Members...)Z
aggressivez[+] Saving In file...zmembers.csv�wzUTF-8)�encoding�,r   )Z	delimiterZlineterminator�usernamezuser idzaccess hash�name�groupzgroup id� z![+] Members scraped successfully.)>Ztelethon.syncr   Ztelethon.tl.functions.messagesr   Ztelethon.tl.typesr   �os�sysZconfigparserZcsvZtimer   Zgrr   r   ZRawConfigParserZcpass�readZapi_idZapi_hashr   Zclient�KeyError�systemr   �exitZconnectZis_user_authorizedZsend_code_requestZsign_in�inputZchatsZ	last_dateZ
chunk_size�groups�result�extendZchatZ	megagroup�append�i�g�str�titleZg_index�intZtarget_groupZsleepZall_participantsZget_participants�open�f�writerZwriterow�userr   Z
first_name�	last_name�stripr   r   Zaccess_hashr	   r	   r	   r
   �<module>   s�   









&


.