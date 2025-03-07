import datetime
from collections.abc import Collection, Iterable, Iterator, MutableMapping, Sequence
from typing import Any, Generic, NoReturn, TypeVar, overload

from _typeshed import Self
from django.db.models import Combinable
from django.db.models.base import Model
from django.db.models.query import QuerySet, RawQuerySet

from django_stubs_ext import ValuesQuerySet

_T = TypeVar("_T", bound=Model, covariant=True)

class BaseManager(Generic[_T]):
    creation_counter: int
    auto_created: bool
    use_in_migrations: bool
    name: str
    model: type[_T]
    _db: str | None
    def __init__(self) -> None: ...
    def deconstruct(
        self,
    ) -> tuple[bool, str | None, str | None, tuple[Any, ...] | None, dict[str, Any] | None]: ...
    def check(self, **kwargs: Any) -> list[Any]: ...
    @classmethod
    def from_queryset(cls, queryset_class: type[QuerySet], class_name: str | None = ...) -> Any: ...
    @classmethod
    def _get_queryset_methods(cls, queryset_class: type) -> dict[str, Any]: ...
    def contribute_to_class(self, cls: type[Model], name: str) -> None: ...
    def db_manager(self: Self, using: str | None = ..., hints: dict[str, Model] | None = ...) -> Self: ...
    @property
    def db(self) -> str: ...
    def get_queryset(self) -> QuerySet[_T]: ...
    # NOTE: The following methods are in common with QuerySet, but note that the use of QuerySet as a return type
    # rather than a self-type (_QS), since Manager's QuerySet-like methods return QuerySets and not Managers.
    def iterator(self, chunk_size: int = ...) -> Iterator[_T]: ...
    async def aiterator(self, chunk_size: int = ...) -> Iterator[_T]: ...
    def aggregate(self, *args: Any, **kwargs: Any) -> dict[str, Any]: ...
    async def aaggregate(self, *args: Any, **kwargs: Any) -> dict[str, Any]: ...
    def get(self, *args: Any, **kwargs: Any) -> _T: ...
    async def aget(self, *args: Any, **kwargs: Any) -> _T: ...
    def create(self, **kwargs: Any) -> _T: ...
    async def acreate(self, **kwargs: Any) -> _T: ...
    def bulk_create(
        self,
        objs: Iterable[_T],
        batch_size: int | None = ...,
        ignore_conflicts: bool = ...,
        update_conflicts: bool = ...,
        update_fields: Collection[str] | None = ...,
        unique_fields: Collection[str] | None = ...,
    ) -> list[_T]: ...
    async def abulk_create(
        self,
        objs: Iterable[_T],
        batch_size: int | None = ...,
        ignore_conflicts: bool = ...,
        update_conflicts: bool = ...,
        update_fields: Collection[str] | None = ...,
        unique_fields: Collection[str] | None = ...,
    ) -> list[_T]: ...
    def bulk_update(self, objs: Iterable[_T], fields: Sequence[str], batch_size: int | None = ...) -> int: ...
    async def abulk_update(self, objs: Iterable[_T], fields: Sequence[str], batch_size: int | None = ...) -> int: ...
    def get_or_create(self, defaults: MutableMapping[str, Any] | None = ..., **kwargs: Any) -> tuple[_T, bool]: ...
    async def aget_or_create(
        self, defaults: MutableMapping[str, Any] | None = ..., **kwargs: Any
    ) -> tuple[_T, bool]: ...
    def update_or_create(self, defaults: MutableMapping[str, Any] | None = ..., **kwargs: Any) -> tuple[_T, bool]: ...
    async def aupdate_or_create(
        self, defaults: MutableMapping[str, Any] | None = ..., **kwargs: Any
    ) -> tuple[_T, bool]: ...
    def earliest(self, *fields: Any, field_name: Any | None = ...) -> _T: ...
    async def aearliest(self, *fields: Any, field_name: Any | None = ...) -> _T: ...
    def latest(self, *fields: Any, field_name: Any | None = ...) -> _T: ...
    async def alatest(self, *fields: Any, field_name: Any | None = ...) -> _T: ...
    def first(self) -> _T | None: ...
    async def afirst(self) -> _T | None: ...
    def last(self) -> _T | None: ...
    async def alast(self) -> _T | None: ...
    def in_bulk(self, id_list: Iterable[Any] = ..., *, field_name: str = ...) -> dict[Any, _T]: ...
    async def ain_bulk(self, id_list: Iterable[Any] = ..., *, field_name: str = ...) -> dict[Any, _T]: ...
    def delete(self) -> tuple[int, dict[str, int]]: ...
    async def adelete(self) -> tuple[int, dict[str, int]]: ...
    def update(self, **kwargs: Any) -> int: ...
    async def aupdate(self, **kwargs: Any) -> int: ...
    def exists(self) -> bool: ...
    async def aexists(self) -> bool: ...
    def explain(self, *, format: Any | None = ..., **options: Any) -> str: ...
    async def aexplain(self, *, format: Any | None = ..., **options: Any) -> str: ...
    def contains(self, objs: Model) -> bool: ...
    async def acontains(self, objs: Model) -> bool: ...
    def raw(
        self,
        raw_query: str,
        params: Any = ...,
        translations: dict[str, str] | None = ...,
        using: str | None = ...,
    ) -> RawQuerySet: ...
    # The type of values may be overridden to be more specific in the mypy plugin, depending on the fields param
    def values(self, *fields: str | Combinable, **expressions: Any) -> ValuesQuerySet[_T, dict[str, Any]]: ...
    # The type of values_list may be overridden to be more specific in the mypy plugin, depending on the fields param
    def values_list(
        self, *fields: str | Combinable, flat: bool = ..., named: bool = ...
    ) -> ValuesQuerySet[_T, Any]: ...
    def dates(self, field_name: str, kind: str, order: str = ...) -> ValuesQuerySet[_T, datetime.date]: ...
    def datetimes(
        self, field_name: str, kind: str, order: str = ..., tzinfo: datetime.tzinfo | None = ...
    ) -> ValuesQuerySet[_T, datetime.datetime]: ...
    def none(self) -> QuerySet[_T]: ...
    def all(self) -> QuerySet[_T]: ...
    def filter(self, *args: Any, **kwargs: Any) -> QuerySet[_T]: ...
    def exclude(self, *args: Any, **kwargs: Any) -> QuerySet[_T]: ...
    def complex_filter(self, filter_obj: Any) -> QuerySet[_T]: ...
    def count(self) -> int: ...
    async def acount(self) -> int: ...
    def union(self, *other_qs: Any, all: bool = ...) -> QuerySet[_T]: ...
    def intersection(self, *other_qs: Any) -> QuerySet[_T]: ...
    def difference(self, *other_qs: Any) -> QuerySet[_T]: ...
    def select_for_update(
        self, nowait: bool = ..., skip_locked: bool = ..., of: Sequence[str] = ..., no_key: bool = ...
    ) -> QuerySet[_T]: ...
    def select_related(self, *fields: Any) -> QuerySet[_T]: ...
    def prefetch_related(self, *lookups: Any) -> QuerySet[_T]: ...
    def annotate(self, *args: Any, **kwargs: Any) -> QuerySet[_T]: ...
    def alias(self, *args: Any, **kwargs: Any) -> QuerySet[_T]: ...
    def order_by(self, *field_names: Any) -> QuerySet[_T]: ...
    def distinct(self, *field_names: Any) -> QuerySet[_T]: ...
    # extra() return type won't be supported any time soon
    def extra(
        self,
        select: dict[str, Any] | None = ...,
        where: list[str] | None = ...,
        params: list[Any] | None = ...,
        tables: list[str] | None = ...,
        order_by: Sequence[str] | None = ...,
        select_params: Sequence[Any] | None = ...,
    ) -> QuerySet[Any]: ...
    def reverse(self) -> QuerySet[_T]: ...
    def defer(self, *fields: Any) -> QuerySet[_T]: ...
    def only(self, *fields: Any) -> QuerySet[_T]: ...
    def using(self, alias: str | None) -> QuerySet[_T]: ...
    @property
    def ordered(self) -> bool: ...

class Manager(BaseManager[_T]): ...

# Fake to make ManyToMany work
class RelatedManager(Manager[_T]):
    related_val: tuple[int, ...]
    def add(self, *objs: _T | int, bulk: bool = ...) -> None: ...
    def remove(self, *objs: _T | int, bulk: bool = ...) -> None: ...
    def set(self, objs: QuerySet[_T] | Iterable[_T | int], *, bulk: bool = ..., clear: bool = ...) -> None: ...
    def clear(self) -> None: ...
    def __call__(self, *, manager: str) -> RelatedManager[_T]: ...

class ManagerDescriptor:
    manager: BaseManager
    def __init__(self, manager: BaseManager) -> None: ...
    @overload
    def __get__(self, instance: None, cls: type[Model] | None = ...) -> BaseManager: ...
    @overload
    def __get__(self, instance: Model, cls: type[Model] | None = ...) -> NoReturn: ...

class EmptyManager(Manager[_T]):
    def __init__(self, model: type[_T]) -> None: ...
