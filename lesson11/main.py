"""
� �������� �� �������� ���� � �����, ��� ���������� ����� ���� "��������".
�� �������, �������� �� ����� ���� ������ ��� � �� ��������.

�� � ���� �������� ������, ���� ������� �� �����. �������, �� ������� �������� ��
�������� �� ����, � ���� ������������ ������������� �������, �� ������� �����
��������. ��� ����� ��� ������� ���� ��������� ���������� ����� (������� ������� �
����� �����, �� �������, ���� ������) �, ������� �� ����������, �������� ������,
�� ��� ������� ������� ��� ����.

������ ������ ���� �������� ��� ������� � �� ��'� �����, � ��� �� ���� ���������
����������. ���������, ���� � ��������� ���������� sort.py, ���, ��� �����������
����� /user/Desktop/������, ����� ��������� ������ ��������
python sort.py /user/Desktop/������

��� ����, ��� ������ ��������� � ��� ���������, �� ������� ������� ����� �������
����� � ������ �������.
��� ������ �� ������ �� ����-��� ������� ����������, ������� ������� �����
������� ���������� ��������� ���� ����, ���� �� ������������ ��������� �����.
������ ������� ��������� �� �������� �� ��� ������� ����� �� ��������� �� ����� �� ������:

���������� ('JPEG', 'PNG', 'JPG', 'SVG');
��������� ('AVI', 'MP4', 'MOV', 'MKV');
��������� ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX');
������ ('MP3', 'OGG', 'WAV', 'AMR');
������ ('ZIP', 'GZ', 'TAR');
������ ����������.
�� ������ ��������� �� ��������� ��� ������, ���� ������.

ϳ��� ��������� ������ �������, �� ������ ��������� �� ������� ������� ���� �����.

��� ����, �� ����� ����� �������������, ��������� �� ����� �� �������, ��
���������� �� �������. ��� ����� ����� ����������� �� ���� ����� ������� normalize.
��� �������, �� ������������� ����� ����� ���, ��� �� ������ ��������� �����,
������ ���� ��������� ��� �� ����� ��������.

������� normalize:
# ����.jpg -> bors�h.jpg
��������� ������������� ����������� ������� �� ����������.
������ �� �������, ��� ���������� ���� �� ����, �� '_'.
������ �� ������� normalize:

������ �� ���� ����� �� ������� �����;
��������� ������������� ���������� ������� �� ��������;
������ �� �������, ��� ���� ����������� ������� �� ����, �� ������ '_';
������������� ���� �� ��������� ���������, ��� ���� �����������;
����� ����� ����������� ��������, � ������� � ���������� ���� �������������.
����� ��� �������:
���������� ���������� �� ����� images
��������� ���������� �� ����� documents
���� ����� ���������� �� audio
���� ����� �� video
������ ��������������, �� �� ���� ������������ �� ����� archives
����� � ��������� ������������ ������� � ����� other
������ ������� ��������
�� ����� ���������������� �� ��������� ������� normalize.
���������� ����� �� ��������� ���� ��������������.
������� ����� �����������
������ ������ ����� archives, video, audio, documents, images, others;
������������ ���� ������ ������������ �� ����� archives � �������, ������� ��� ����,
�� � �����, ��� ��� ���������� � ����. ������� ������, �� �� ��������������, ����� ��������;
� ����������� ������ ������� ����:

������ ����� � ������ ������� (������, ����, ���� �� ��.)
������ ��� ������ ������� ���������, �� ������������ � ������� �����.
������ ��� ���������, �� ������� ������.
��� ��������� ��� ������� � �������, ��� �������� � ����.
"""

