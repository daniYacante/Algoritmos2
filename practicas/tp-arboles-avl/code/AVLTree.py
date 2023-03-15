


class AVLTree:
    root=None


class AVLNode:
    parent=None
    leftnode=None
    rightnode=None
    key=None
    bf=None


def rotateLeft(tree:AVLTree,avlnode:AVLNode):
    nodoActual=avlnode
    hijoDer=nodoActual.rightnode
    padre=nodoActual.parent
    if hijoDer.leftnode!=None:
        nodoActual.rightnode=hijoDer.leftnode
    hijoDer.leftnode=nodoActual
    if padre!=None:
        if padre.rightnode==nodoActual:
            padre.rightnode=hijoDer
        else:
            padre.leftnode=hijoDer
    return tree.root


def rotateRight(tree:AVLTree,avlnode:AVLNode):
    nodoActual=avlnode
    hijoIzq=nodoActual.leftnode
    padre=nodoActual.parent
    if hijoIzq.rightnode!=None:
        nodoActual.leftnode=hijoIzq.rightnode
    hijoIzq.rightnode=nodoActual
    if padre!=None:
        if padre.rightnode==nodoActual:
            padre.rightnode=hijoIzq
        else:
            padre.leftnode=hijoIzq
    return tree.root